import re

from production_code.common.parser import Parser
from production_code.common.constants import Constants as CommonConstants
from production_code.MRS.common.constants import Constants


class MRSParser(Parser):
    def _get_justified_close_locations(self):
        raise NotImplementedError("Must be implemented")

    def _get_incorrect_gps(self):
        raise NotImplementedError("Must be implemented")

    def _get_locations_list_url(self):
        raise NotImplementedError("Must be implemented")

    def _get_location_url_pattern(self):
        raise NotImplementedError("Must be implemented")

    def _get_location_id(self, context):
        return re.search(Constants.LOCATION_ID_PATTERN, context).group(
            CommonConstants.LOCATION_ID_PATTERN_GROUP_NAME)

    def _get_location_name(self, context):
        return re.search(Constants.LOCATION_NAME_PATTERN, context).group(
            CommonConstants.LOCATION_NAME_PATTERN_GROUP_NAME)

    def _get_headquarter(self, context):
        return re.search(Constants.HEADQUARTER_PATTERN, context).group(
            CommonConstants.HEADQUARTER_PATTERN_GROUP_NAME)

    def _get_area(self, context):
        return re.search(Constants.AREA_PATTERN, context).group(
            CommonConstants.AREA_PATTERN_GROUP_NAME)

    def _get_locations_url(self):
        locations_url = []
        decoded_page = self._get_decoded_source_page(
            self._get_locations_list_url())
        for match in re.finditer(self._get_location_url_pattern(), decoded_page):
            locations_url.append(
                Constants.MRS_HOME_PAGE
                + match.group(CommonConstants.LOCATION_URL_PATTERN_GROUP_NAME))
        return locations_url
