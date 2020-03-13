from production_code.CRS.NorthMoraviaAndSilesia.common.parser import NorthMoraviaAndSilesiaParser
from production_code.CRS.NorthMoraviaAndSilesia.non_salmonid.constants import NorthMoraviaAndSilesiaConstants


class NorthMoraviaAndSilesiaNonSalmonidParser(NorthMoraviaAndSilesiaParser):
    def _get_justified_close_locations(self):
        return NorthMoraviaAndSilesiaConstants.JUSTIFIED_CLOSE_LOCATIONS

    def _get_incorrect_gps(self):
        return NorthMoraviaAndSilesiaConstants.INCORRECT_GPS

    def _get_headquarter_gps(self, headquarter):
        return NorthMoraviaAndSilesiaConstants.HEADQUARTER_GPS[headquarter]

    @staticmethod
    def _get_locations_per_page():
        return NorthMoraviaAndSilesiaConstants.LOCATIONS_PER_PAGE

    @staticmethod
    def _get_location_url_pattern():
        return NorthMoraviaAndSilesiaConstants.LOCATION_URL_PATTERN
