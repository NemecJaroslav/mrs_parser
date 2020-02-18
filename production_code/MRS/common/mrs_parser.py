import re

from production_code.common.parser import Parser
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

    def _get_locations_url(self):
        locations_url = []
        decoded_page = Parser._get_decoded_source_page(
            self._get_locations_list_url())
        for match in re.finditer(self._get_location_url_pattern(), decoded_page):
            locations_url.append(
                Constants.MRS_HOME_PAGE
                + match.group(Constants.LOCATION_URL_PATTERN_GROUP_NAME))
        return locations_url
