from production_code.MRS.common.mrs_parser import MRSParser
from .constants import SalmonidConstants
from .justified_close_locations import justified_close_locations


class SalmonidParser(MRSParser):
    def __init__(self):
        super(SalmonidParser, self).__init__()

    def _get_locations_list_url(self):
        return SalmonidConstants.LOCATIONS_LIST_URL

    def _get_location_url_pattern(self):
        return SalmonidConstants.LOCATION_URL_PATTERN

    def _get_incorrect_gps(self):
        return SalmonidConstants.INCORRECT_GPS

    def _get_justified_close_locations(self):
        return justified_close_locations
