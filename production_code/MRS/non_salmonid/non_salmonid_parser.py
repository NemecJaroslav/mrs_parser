from production_code.MRS.common.mrs_parser import MRSParser
from .constants import NonSalmonidConstants
from .justified_close_locations import justified_close_locations


class NonSalmonidParser(MRSParser):
    def _get_justified_close_locations(self):
        return justified_close_locations

    def _get_incorrect_gps(self):
        return NonSalmonidConstants.INCORRECT_GPS

    def _get_headquarter_gps(self, headquarter):
        return NonSalmonidConstants.HEADQUARTER_GPS[headquarter]

    def _get_locations_list_url(self):
        return NonSalmonidConstants.LOCATIONS_LIST_URL

    def _get_location_url_pattern(self):
        return NonSalmonidConstants.LOCATION_URL_PATTERN
