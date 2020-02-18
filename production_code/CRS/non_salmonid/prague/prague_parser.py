from production_code.CRS.common.crs_parser import CRSParser
from production_code.CRS.non_salmonid.prague.prague_constants import PragueConstants


class PragueParser(CRSParser):
    def _get_justified_close_locations(self):
        return []

    def _get_incorrect_gps(self):
        return []

    def _get_locations_list_url(self):
        return PragueConstants.LOCATIONS_LIST_URL
