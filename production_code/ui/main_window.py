import io
import sys
import folium

from production_code.fishing_locations_interface.api import (
    get_available_organisations, get_suitable_fishing_locations, get_all_headquarters,
    get_total_area_for_given_headquarter, get_fishing_locations_for_given_headquarter, prepare_parser)
from production_code.common.distance_limit import DistanceLimit

from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QApplication, QVBoxLayout, QPushButton, QHBoxLayout, QComboBox, QLabel, QLineEdit,
    QTableWidget, QTableWidgetItem, QFormLayout, QAbstractItemView, QHeaderView,
)
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtGui import QDoubleValidator, QIntValidator


# https://realpython.com/python-pyqt-gui-calculator/
class FishingLocationsMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fishing Locations")
        self._centralWidget = FishingLocationsWidget(self)
        self.setCentralWidget(self._centralWidget)
        self.show()


class FishingLocationsWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.mapWidget = QWebEngineView()
        self.layout.addWidget(self.mapWidget)
        self.setLayout(self.layout)

        current_position = [49.1806731, 16.6801281]

        self.map = None
        self._create_map(current_position)

        self._suitable_fishing_position_markers = []

        self._choose_organization_combo_box = QComboBox()
        self._choose_organization_combo_box.currentIndexChanged.connect(self._organisation_changed)
        self._choose_current_position_latitude = QLineEdit(str(current_position[0]))
        self._choose_current_position_latitude.setValidator(QDoubleValidator())
        self._choose_current_position_longitude = QLineEdit(str(current_position[1]))
        self._choose_current_position_longitude.setValidator(QDoubleValidator())
        self._choose_distance_limit_min = QLineEdit()
        self._choose_distance_limit_min.setValidator(QIntValidator())
        self._choose_distance_limit_max = QLineEdit()
        self._choose_distance_limit_max.setValidator(QIntValidator())
        self._look_for_suitable_fishing_locations_button = QPushButton("Search")
        self._look_for_suitable_fishing_locations_button.clicked.connect(self._button_clicked)
        self._suitable_locations_table = QTableWidget()
        self._suitable_locations_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self._suitable_locations_table.clicked.connect(self._suitable_location_selected)

        self._choose_headquarters_combo_box = QComboBox()
        self._choose_headquarters_combo_box.currentTextChanged.connect(self._headquarter_changed)
        self._headquarter_locations_table = QTableWidget()
        self._headquarter_locations_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self._add_current_position_marker()
        self._place_ui_elements()

        self._fill_organisation_combo_box(get_available_organisations())

    def _place_ui_elements(self):
        outer_layout = QVBoxLayout()
        organization_layout = QFormLayout()
        organization_layout.addRow("Choose organisation:", self._choose_organization_combo_box)

        suitable_locations_vs_headquarters_layout = QHBoxLayout()

        suitable_locations_layout = QVBoxLayout()

        current_position_layout = QFormLayout()
        latitude_and_longitude_layout = QHBoxLayout()
        latitude_and_longitude_layout.addWidget(self._choose_current_position_latitude)
        latitude_and_longitude_layout.addWidget(self._choose_current_position_longitude)
        current_position_layout.addRow("Choose current position (lat, lon):", latitude_and_longitude_layout)
        suitable_locations_layout.addLayout(current_position_layout)

        distance_layout = QFormLayout()
        min_max_distance_layout = QHBoxLayout()
        min_max_distance_layout.addWidget(self._choose_distance_limit_min)
        min_max_distance_layout.addWidget(self._choose_distance_limit_max)
        distance_layout.addRow("Choose distance limit (min, max) [km]:", min_max_distance_layout)
        suitable_locations_layout.addLayout(distance_layout)

        suitable_locations_layout.addWidget(self._look_for_suitable_fishing_locations_button)
        suitable_locations_layout.addWidget(self._suitable_locations_table)

        suitable_locations_vs_headquarters_layout.addLayout(suitable_locations_layout)

        # headquarters
        headquarters_layout = QVBoxLayout()
        headquarters_combo_layout = QFormLayout()
        headquarters_combo_layout.addRow("Choose headquarters:", self._choose_headquarters_combo_box)
        headquarters_layout.addLayout(headquarters_combo_layout)

        headquarters_layout.addWidget(self._headquarter_locations_table)

        suitable_locations_vs_headquarters_layout.addLayout(headquarters_layout)

        outer_layout.addLayout(organization_layout)
        outer_layout.addLayout(suitable_locations_vs_headquarters_layout)
        self.layout.addLayout(outer_layout)

    def _redraw_map(self):
        data = io.BytesIO()
        self.map.save(data, close_file=False)
        self.mapWidget.setHtml(data.getvalue().decode())

    def _create_map(self, current_position):
        self.map = folium.Map(tiles="Stamen Terrain", zoom_start=13, location=current_position)
        marker = folium.Marker(current_position, popup="Current position", icon=folium.Icon(icon="car", prefix="fa"))
        marker.add_to(self.map)
        self._redraw_map()

    def _add_suitable_fishing_position_markers(self, records):
        for record in records:
            marker = folium.Marker(
                [record.gps[0], record.gps[1]], popup=record.name + ", " + self._format_float(record.distance) + " km")
            self._suitable_fishing_position_markers.append(marker)
            self._suitable_fishing_position_markers[-1].add_to(self.map)
        self._redraw_map()

    def _delete_suitable_fishing_position_markers(self):
        self._suitable_fishing_position_markers = []

    def _add_current_position_marker(self):
        current_position = [float(self._choose_current_position_latitude.text()),
                            float(self._choose_current_position_longitude.text())]
        self._create_map(current_position)

    def _suitable_location_selected(self, index):
        marker = self._suitable_fishing_position_markers[index.row()]
        self.map.location = marker.location
        self._redraw_map()

    # TODO: implement
    def _add_headquarter_fishing_location_markers(self, records):
        return
        # for record in records:
        #     for c1, c2 in record.gps_locations:
        #         marker = folium.CircleMarker([c1.convert_to_dd(), c2.convert_to_dd()], popup=record.name)

    def _fill_suitable_locations_table(self, records):
        self._suitable_locations_table.setRowCount(len(records))
        self._suitable_locations_table.setColumnCount(5)
        self._suitable_locations_table.setHorizontalHeaderLabels(
            ["Identifier", "Name", "Headquarter", "GPS", "Distance [km]"])
        for row_index, record in enumerate(records):
            self._suitable_locations_table.setItem(row_index, 0, QTableWidgetItem(record.id))
            self._suitable_locations_table.setItem(row_index, 1, QTableWidgetItem(record.name))
            self._suitable_locations_table.setItem(row_index, 2, QTableWidgetItem(record.headquarter))
            self._suitable_locations_table.setItem(row_index, 3, QTableWidgetItem(self._format_dd(record.gps)))
            self._suitable_locations_table.setItem(row_index, 4, QTableWidgetItem(self._format_float(record.distance)))

    def _fill_headquarter_locations_table(self, headquarter, records):
        self._headquarter_locations_table.clear()
        self._headquarter_locations_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self._headquarter_locations_table.horizontalHeader().setStretchLastSection(True)
        self._headquarter_locations_table.setRowCount(len(records) + 1)
        self._headquarter_locations_table.setColumnCount(3)
        self._headquarter_locations_table.setHorizontalHeaderLabels(
            ["Identifier", "Name", "Area [ha]"])
        for row_index, record in enumerate(records):
            self._headquarter_locations_table.setItem(row_index, 0, QTableWidgetItem(record.identifier))
            self._headquarter_locations_table.setItem(row_index, 1, QTableWidgetItem(record.name))
            self._headquarter_locations_table.setItem(row_index, 2, QTableWidgetItem(self._format_float(record.area)))

        self._headquarter_locations_table.setItem(
            len(records), 2, QTableWidgetItem(
                str(get_total_area_for_given_headquarter(
                    self._choose_organization_combo_box.currentIndex(), headquarter))))

    def _fill_organisation_combo_box(self, organizations):
        self._choose_organization_combo_box.addItems(organizations)

    def _fill_headquarters_combo_box(self, headquarters):
        self._choose_headquarters_combo_box.clear()
        self._choose_headquarters_combo_box.addItems(headquarters)

    def _organisation_changed(self, index):
        prepare_parser(index)
        self._start_searching_for_suitable_fishing_locations(index)
        self._fill_headquarters_combo_box(get_all_headquarters(index))

    def _headquarter_changed(self, headquarter):
        records = get_fishing_locations_for_given_headquarter(
            self._choose_organization_combo_box.currentIndex(), headquarter)
        self._fill_headquarter_locations_table(headquarter, records)
        self._add_headquarter_fishing_location_markers(records)

    def _button_clicked(self, checked):
        self._start_searching_for_suitable_fishing_locations(self._choose_organization_combo_box.currentIndex())

    def _start_searching_for_suitable_fishing_locations(self, index):
        if self._can_suitable_locations_table_be_filled():
            self._delete_suitable_fishing_position_markers()
            self._add_current_position_marker()
            self._prepare_suitable_fishing_locations_table()

            suitable_fishing_locations = self._get_suitable_fishing_locations(index)
            self._fill_suitable_locations_table(suitable_fishing_locations)
            self._add_suitable_fishing_position_markers(suitable_fishing_locations)

    def _prepare_suitable_fishing_locations_table(self):
        self._suitable_locations_table.clear()
        self._suitable_locations_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self._suitable_locations_table.horizontalHeader().setStretchLastSection(True)

    def _get_suitable_fishing_locations(self, index):
        return get_suitable_fishing_locations(
                index, (float(self._choose_current_position_latitude.text()),
                        float(self._choose_current_position_longitude.text())),
                DistanceLimit(float(self._choose_distance_limit_min.text()),
                              float(self._choose_distance_limit_max.text())))

    def _can_suitable_locations_table_be_filled(self):
        return (self._choose_current_position_latitude.text()
                and self._choose_current_position_longitude.text()
                and self._choose_distance_limit_min.text()
                and self._choose_distance_limit_max.text())

    def _format_dd(self, dd):
        return "(" + self._format_float(dd[0]) + ", " + self._format_float(dd[1]) + ")"

    @staticmethod
    def _format_float(number):
        return "{:.3f}".format(number)


def main():
    fishing_locations = QApplication(sys.argv)
    view = FishingLocationsMainWindow()
    view.show()
    sys.exit(fishing_locations.exec_())


if __name__ == "__main__":
    main()
