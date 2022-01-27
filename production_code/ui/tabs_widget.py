from production_code.common.distance_limit import DistanceLimit
from production_code.ui.format_strings import format_float, format_dd

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLineEdit, QTableWidget, QTableWidgetItem, QFormLayout,
    QAbstractItemView, QHeaderView, QTabWidget)

from PyQt5.QtGui import QDoubleValidator, QIntValidator


class TabsWidget(QTabWidget):
    def __init__(
            self, current_location, search_button_clicked_callback, suitable_fishing_location_selected_callback):
        super().__init__()
        self._search_button_clicked_callback = search_button_clicked_callback
        self._suitable_fishing_location_selected_callback = suitable_fishing_location_selected_callback
        self.layout = QVBoxLayout(self)

        self._suitable_fishing_locations_tab = QWidget()
        self._create_suitable_fishing_locations_tab_elements(current_location)
        self._set_suitable_fishing_locations_tab_layout()

        self.addTab(self._suitable_fishing_locations_tab, "Suitable fishing locations")
        self.setLayout(self.layout)

    def search_for_suitable_fishing_locations(self):
        if (self._choose_current_position_latitude.text()
                and self._choose_current_position_longitude.text()
                and self._choose_distance_limit_min.text()
                and self._choose_distance_limit_max.text()):
            current_position = (float(self._choose_current_position_latitude.text()),
                                float(self._choose_current_position_longitude.text()))
            distance_limit = DistanceLimit(float(self._choose_distance_limit_min.text()),
                                           float(self._choose_distance_limit_max.text()))
            self._search_button_clicked_callback(current_position, distance_limit)

    def show_suitable_fishing_locations(self, records):
        self._suitable_locations_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self._suitable_locations_table.setRowCount(len(records))
        self._suitable_locations_table.setColumnCount(5)
        self._suitable_locations_table.setHorizontalHeaderLabels(
            ["Identifier", "Name", "Headquarter", "GPS", "Distance [km]"])
        for row_index, record in enumerate(records):
            self._suitable_locations_table.setItem(row_index, 0, QTableWidgetItem(record.id))
            self._suitable_locations_table.setItem(row_index, 1, QTableWidgetItem(record.name))
            self._suitable_locations_table.setItem(row_index, 2, QTableWidgetItem(record.headquarter))
            self._suitable_locations_table.setItem(row_index, 3, QTableWidgetItem(format_dd(record.gps)))
            self._suitable_locations_table.setItem(row_index, 4, QTableWidgetItem(format_float(record.distance)))

    def _create_suitable_fishing_locations_tab_elements(self, current_location):
        self._choose_current_position_latitude = QLineEdit(str(current_location[0]))
        self._choose_current_position_latitude.setValidator(QDoubleValidator())
        self._choose_current_position_longitude = QLineEdit(str(current_location[1]))
        self._choose_current_position_longitude.setValidator(QDoubleValidator())

        self._choose_distance_limit_min = QLineEdit()
        self._choose_distance_limit_min.setValidator(QIntValidator())
        self._choose_distance_limit_max = QLineEdit()
        self._choose_distance_limit_max.setValidator(QIntValidator())
        self._look_for_suitable_fishing_locations_button = QPushButton("Search")
        self._look_for_suitable_fishing_locations_button.clicked.connect(self.search_for_suitable_fishing_locations)
        self._suitable_locations_table = QTableWidget()
        self._suitable_locations_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self._suitable_locations_table.clicked.connect(self._suitable_fishing_location_selected)

    def _set_suitable_fishing_locations_tab_layout(self):
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

        self._suitable_fishing_locations_tab.setLayout(suitable_locations_layout)

    def _suitable_fishing_location_selected(self, selection):
        self._suitable_fishing_location_selected_callback(selection.row())
