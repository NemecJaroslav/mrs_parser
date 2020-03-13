from production_code.CRS.NorthMoraviaAndSilesia.common.parser import NorthMoraviaAndSilesiaParser
from production_code.CRS.NorthMoraviaAndSilesia.salmonid.constants import NorthMoraviaAndSilesiaSalmonidConstants


class NorthMoraviaAndSilesiaSalmonidParser(NorthMoraviaAndSilesiaParser):
    def _get_justified_close_locations(self):
        raise NotImplementedError("Must be implemented")

    def _get_incorrect_gps(self):
        return NorthMoraviaAndSilesiaSalmonidConstants.INCORRECT_GPS

    def _get_headquarter_gps(self, headquarter):
        raise NotImplementedError("Must be implemented")

    @staticmethod
    def _get_locations_per_page():
        return NorthMoraviaAndSilesiaSalmonidConstants.LOCATIONS_PER_PAGE

    @staticmethod
    def _get_location_url_pattern():
        return NorthMoraviaAndSilesiaSalmonidConstants.LOCATION_URL_PATTERN
