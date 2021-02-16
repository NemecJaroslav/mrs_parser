from production_code.CRS.NorthMoraviaAndSilesia.common.parser import NorthMoraviaAndSilesiaParser
from production_code.CRS.NorthMoraviaAndSilesia.salmonid.constants import (
    NorthMoraviaAndSilesiaSalmonidConstants)


class NorthMoraviaAndSilesiaSalmonidParser(NorthMoraviaAndSilesiaParser):
    @staticmethod
    def get_parser_description():
        return "CRS - Severni Morava a Slezsko (pstruhove)"

    def _get_justified_close_locations(self):
        return NorthMoraviaAndSilesiaSalmonidConstants.JUSTIFIED_CLOSE_LOCATIONS

    def _get_incorrect_gps(self):
        return NorthMoraviaAndSilesiaSalmonidConstants.INCORRECT_GPS

    def _get_headquarter_gps(self, headquarter):
        return NorthMoraviaAndSilesiaSalmonidConstants.HEADQUARTER_GPS[headquarter]

    @staticmethod
    def _get_locations_per_page():
        return NorthMoraviaAndSilesiaSalmonidConstants.LOCATIONS_PER_PAGE

    @staticmethod
    def _get_location_url_pattern():
        return NorthMoraviaAndSilesiaSalmonidConstants.LOCATION_URL_PATTERN
