from production_code.MRS.common.mrs_parser import MRSParser
from .constants import SalmonidConstants
from .justified_close_locations import justified_close_locations


class SalmonidParser(MRSParser):
    @staticmethod
    def get_parser_description():
        return "MRS (pstruhove)"

    def _get_justified_close_locations(self):
        return justified_close_locations

    def _get_incorrect_gps(self):
        return SalmonidConstants.INCORRECT_GPS

    def _get_headquarter_gps(self, headquarter):
        return SalmonidConstants.HEADQUARTER_GPS[headquarter]

    def _get_locations_list_url(self):
        return SalmonidConstants.LOCATIONS_LIST_URL

    def _get_location_url_pattern(self):
        return SalmonidConstants.LOCATION_URL_PATTERN
