from production_code.common.mrs_parser import MRSParser
from .constants import NonSalmonidConstants
from .justified_close_locations import justified_close_locations


class NonSalmonidParser(MRSParser):
    def __init__(self):
        super(NonSalmonidParser, self).__init__()

    def _get_locations_list_url(self):
        return NonSalmonidConstants.LOCATIONS_LIST_URL

    def _get_location_url_pattern(self):
        return NonSalmonidConstants.LOCATION_URL_PATTERN

    def _get_incorrect_gps(self):
        return NonSalmonidConstants.INCORRECT_GPS

    def _get_justified_close_locations(self):
        return justified_close_locations
