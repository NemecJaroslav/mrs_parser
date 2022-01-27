from production_code.fishing_locations_interface.api import get_available_organisations

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QComboBox


class OrganisationsWidget(QWidget):
    def __init__(self, organisation_changed_callback):
        super().__init__()
        self._organisation_changed_callback = organisation_changed_callback
        self.layout = QVBoxLayout(self)
        self._choose_organization_combo_box = QComboBox()
        self._choose_organization_combo_box.addItems(get_available_organisations())
        self._choose_organization_combo_box.currentIndexChanged.connect(self._organisation_changed)
        self._organisation_changed(self._choose_organization_combo_box.currentIndex())
        self.layout.addWidget(self._choose_organization_combo_box)
        self.setLayout(self.layout)

    def _organisation_changed(self, organisation_index):
        self._organisation_changed_callback(organisation_index)
