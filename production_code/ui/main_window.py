import sys

from production_code.fishing_locations_interface.api import (
    get_available_organisations, get_suitable_fishing_locations, prepare_parser)
from production_code.common.distance_limit import DistanceLimit

from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QApplication, QVBoxLayout, QTabWidget, QPushButton, QHBoxLayout, QComboBox, QLabel, QLineEdit,
    QTableWidget, QTableWidgetItem
)

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

        self._tabs = QTabWidget()
        self._location_tab = QWidget()
        self._headquarter_tab = QWidget()
        self._choose_organization_label = QLabel("Choose organisation:")
        self._choose_organization_combo_box = QComboBox()
        self._choose_organization_combo_box.currentIndexChanged.connect(self._organisation_changed)
        self._choose_current_position_label = QLabel("Choose current position (lat, lon):")
        self._choose_current_position_latitude = QLineEdit("49.1806731")
        self._choose_current_position_latitude.setValidator(QDoubleValidator())
        self._choose_current_position_longitude = QLineEdit("16.6801281")
        self._choose_current_position_longitude.setValidator(QDoubleValidator())
        self._choose_distance_limit_label = QLabel("Choose distance limit (min, max) in km:")
        self._choose_distance_limit_min = QLineEdit()
        self._choose_distance_limit_min.setValidator(QIntValidator())
        self._choose_distance_limit_max = QLineEdit()
        self._choose_distance_limit_max.setValidator(QIntValidator())
        self._look_for_suitable_fishing_locations_button = QPushButton("Search")
        self._look_for_suitable_fishing_locations_button.clicked.connect(self._button_clicked)
        self._suitable_locations_table = QTableWidget()

        self._add_tabs()
        self._initialize_locations_tab()
        self._initialize_headquarters_tab()

        self._fill_organisation_combo_box(get_available_organisations())

        self.layout.addWidget(self._tabs)
        self.setLayout(self.layout)

    def _add_tabs(self):
        self._tabs.addTab(self._location_tab, "Locations")
        self._tabs.addTab(self._headquarter_tab, "Headquarters")

    def _initialize_locations_tab(self):
        self._location_tab.layout = QVBoxLayout(self)
        self._location_tab.layout.addWidget(self._choose_organization_label)
        self._location_tab.layout.addWidget(self._choose_organization_combo_box)
        self._location_tab.layout.addWidget(self._choose_current_position_label)
        self._location_tab.layout.addWidget(self._choose_current_position_latitude)
        self._location_tab.layout.addWidget(self._choose_current_position_longitude)
        self._location_tab.layout.addWidget(self._choose_distance_limit_label)
        self._location_tab.layout.addWidget(self._choose_distance_limit_min)
        self._location_tab.layout.addWidget(self._choose_distance_limit_max)
        self._location_tab.layout.addWidget(self._look_for_suitable_fishing_locations_button)
        self._location_tab.layout.addWidget(self._suitable_locations_table)
        self._location_tab.setLayout(self._location_tab.layout)

    def _initialize_headquarters_tab(self):
        pass

    def _fill_suitable_locations_table(self, index):
        records = self._get_suitable_fishing_locations(index)
        self._suitable_locations_table.setRowCount(len(records))
        self._suitable_locations_table.setColumnCount(5)
        for row_index, record in enumerate(records):
            self._suitable_locations_table.setItem(row_index, 0, QTableWidgetItem(record.id))
            self._suitable_locations_table.setItem(row_index, 1, QTableWidgetItem(record.name))
            self._suitable_locations_table.setItem(row_index, 2, QTableWidgetItem(record.headquarter))
            self._suitable_locations_table.setItem(row_index, 3, QTableWidgetItem(str(record.gps)))
            self._suitable_locations_table.setItem(row_index, 4, QTableWidgetItem(str(record.distance)))

    def _fill_organisation_combo_box(self, organizations):
        self._choose_organization_combo_box.addItems(organizations)

    def _organisation_changed(self, index):
        prepare_parser(index)
        self._fill_suitable_locations_table(index)

    def _button_clicked(self, checked):
        self._fill_suitable_locations_table(self._choose_organization_combo_box.currentIndex())

    def _get_suitable_fishing_locations(self, index):
        if self._can_suitable_locations_table_be_filled():
            return get_suitable_fishing_locations(
                    index, (float(self._choose_current_position_latitude.text()),
                            float(self._choose_current_position_longitude.text())),
                    DistanceLimit(float(self._choose_distance_limit_min.text()),
                                  float(self._choose_distance_limit_max.text())))
        return list()

    def _can_suitable_locations_table_be_filled(self):
        return (self._choose_current_position_latitude.text()
                and self._choose_current_position_longitude.text()
                and self._choose_distance_limit_min.text()
                and self._choose_distance_limit_max.text())


def main():
    fishing_locations = QApplication(sys.argv)
    view = FishingLocationsMainWindow()
    view.show()
    sys.exit(fishing_locations.exec_())


if __name__ == "__main__":
    main()
