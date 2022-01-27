import sys

from production_code.fishing_locations_interface.api import prepare_parser, get_suitable_fishing_locations

from production_code.ui.map import Map
from production_code.ui.organisations_widget import OrganisationsWidget
from production_code.ui.tabs_widget import TabsWidget

from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QVBoxLayout


class FishingLocationsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fishing Locations")
        self._centralWidget = FishingLocationsWidget(self)
        self.setCentralWidget(self._centralWidget)
        self.showMaximized()
        self.show()


class FishingLocationsWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        current_location = [49.1806731, 16.6801281]
        self._organisation_index = 0
        self.layout = QVBoxLayout(self)
        self.mapWidget = Map(current_location)
        self.tabsWidget = TabsWidget(
            current_location, self._search_button_clicked, self._suitable_fishing_location_selected)
        self.organizationsWidget = OrganisationsWidget(self._organisation_changed)

        self.layout.addWidget(self.mapWidget)
        self.layout.addWidget(self.organizationsWidget)
        self.layout.addWidget(self.tabsWidget)
        self.setLayout(self.layout)

    def _organisation_changed(self, organisation_index):
        self._organisation_index = organisation_index
        prepare_parser(self._organisation_index)
        # TODO: I don't like that I have search_for_suitable_fishing_locations and show_suitable_fishing_locations
        self.tabsWidget.search_for_suitable_fishing_locations()

    def _search_button_clicked(self, start_point, distance_limit):
        suitable_fishing_locations = get_suitable_fishing_locations(
            self._organisation_index, start_point, distance_limit)
        self.mapWidget.show_suitable_fishing_locations(start_point, suitable_fishing_locations)
        self.tabsWidget.show_suitable_fishing_locations(suitable_fishing_locations)

    def _suitable_fishing_location_selected(self, fishing_location_index):
        self.mapWidget.show_particular_fishing_location(fishing_location_index)


def main():
    fishing_locations = QApplication(sys.argv)
    view = FishingLocationsWindow()
    view.show()
    sys.exit(fishing_locations.exec_())


if __name__ == "__main__":
    main()
