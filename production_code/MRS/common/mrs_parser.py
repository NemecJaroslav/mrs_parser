import re

from production_code.common.parser import Parser
from production_code.MRS.common.constants import MRSConstants


class MRSParser(Parser):
    def _get_justified_close_locations(self):
        raise NotImplementedError("Must be implemented")

    def _get_locations_url(self):
        locations_url = []
        decoded_page = self._get_decoded_source_page(
            self._get_locations_list_url())
        for match in re.finditer(self._get_location_url_pattern(), decoded_page):
            locations_url.append(
                MRSConstants.MRS_HOME_PAGE
                + self._get_location_url(match))
        return locations_url

    def _get_incorrect_gps(self):
        raise NotImplementedError("Must be implemented")

    def _get_headquarter_gps(self, headquarter):
        raise NotImplementedError("Must be implemented")

    def _get_locations_list_url(self):
        raise NotImplementedError("Must be implemented")

    def _get_location_url_pattern(self):
        raise NotImplementedError("Must be implemented")

    @staticmethod
    def _get_location_id(context, location_id_pattern=MRSConstants.LOCATION_ID_PATTERN):
        return Parser._get_location_id(context, location_id_pattern)

    @staticmethod
    def _get_location_name(context, location_name_pattern=MRSConstants.LOCATION_NAME_PATTERN):
        return Parser._get_location_name(context, location_name_pattern)

    @staticmethod
    def _get_headquarter(context, headquarter_pattern=MRSConstants.HEADQUARTER_PATTERN):
        return Parser._get_headquarter(context, headquarter_pattern)

    @staticmethod
    def _get_area(context, area_pattern=MRSConstants.AREA_PATTERN):
        return Parser._get_area(context, area_pattern)
