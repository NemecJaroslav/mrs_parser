import re

from production_code.common.parser import Parser
from production_code.common.constants import Constants

from production_code.CRS.non_salmonid.NorthMoraviaAndSilesia.constants import NorthMoraviaAndSilesiaConstants


class NorthMoraviaAndSilesiaParser(Parser):
    def _get_justified_close_locations(self):
        return NorthMoraviaAndSilesiaConstants.JUSTIFIED_CLOSE_LOCATIONS

    def _get_location_url_pattern(self):
        return NorthMoraviaAndSilesiaConstants.LOCATION_URL_PATTERN

    def _get_locations_url(self):
        locations_url = []
        for location_list in NorthMoraviaAndSilesiaConstants.LOCATIONS_PER_PAGE:
            decoded_page = self._get_decoded_source_page(location_list)
            for match in re.finditer(self._get_location_url_pattern(), decoded_page):
                locations_url.append(
                    NorthMoraviaAndSilesiaConstants.NORTHMORAVIAANDSILESIA_HOME_PAGE
                    + match.group(Constants.LOCATION_URL_PATTERN_GROUP_NAME))
        return sorted(set(locations_url))

    def _get_incorrect_gps(self):
        return NorthMoraviaAndSilesiaConstants.INCORRECT_GPS

    def _get_location_id(self, context):
        return re.search(NorthMoraviaAndSilesiaConstants.LOCATION_ID_PATTERN, context).group(
            Constants.LOCATION_ID_PATTERN_GROUP_NAME)

    def _get_location_name(self, context):
        return re.search(NorthMoraviaAndSilesiaConstants.LOCATION_NAME_PATTERN, context).group(
            Constants.LOCATION_NAME_PATTERN_GROUP_NAME)

    def _get_headquarter(self, context):
        return re.search(NorthMoraviaAndSilesiaConstants.HEADQUARTER_PATTERN, context).group(
            Constants.HEADQUARTER_PATTERN_GROUP_NAME)

    def _get_area(self, context):
        search_result = re.search(NorthMoraviaAndSilesiaConstants.AREA_PATTERN, context)
        if search_result is None:
            print(NorthMoraviaAndSilesiaConstants.EMPTY_AREA_WARNING)
            return NorthMoraviaAndSilesiaConstants.EMPTY_AREA
        return search_result.group(Constants.AREA_PATTERN_GROUP_NAME)
