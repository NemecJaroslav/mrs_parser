import re

from production_code.common.parser import Parser
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
                    + self._get_location_url(match))
        return sorted(set(locations_url))

    def _get_incorrect_gps(self):
        return NorthMoraviaAndSilesiaConstants.INCORRECT_GPS

    @staticmethod
    def _get_location_id(context, location_id_pattern=NorthMoraviaAndSilesiaConstants.LOCATION_ID_PATTERN):
        return Parser._get_location_id(context, location_id_pattern)

    @staticmethod
    def _get_location_name(context, location_name_pattern=NorthMoraviaAndSilesiaConstants.LOCATION_NAME_PATTERN):
        return Parser._get_location_name(context, location_name_pattern)

    @staticmethod
    def _get_headquarter(context, headquarter_pattern=NorthMoraviaAndSilesiaConstants.HEADQUARTER_PATTERN):
        return Parser._get_headquarter(context, headquarter_pattern)

    @staticmethod
    def _get_area(context, area_pattern=NorthMoraviaAndSilesiaConstants.AREA_PATTERN):
        return Parser._get_area(context, area_pattern)
