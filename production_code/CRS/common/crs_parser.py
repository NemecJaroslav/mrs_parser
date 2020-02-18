import re
import requests

from production_code.common.parser import Parser
from production_code.CRS.common.constants import Constants


class CRSParser(Parser):
    @staticmethod
    def _get_decoded_source_page(url):
        return requests.get(url).content.decode("latin-1")

    def _get_justified_close_locations(self):
        raise NotImplementedError("Must be implemented")

    def _get_incorrect_gps(self):
        raise NotImplementedError("Must be implemented")

    def _get_location_url_pattern(self):
        return Constants.LOCATION_URL_PATTERN

    def _get_locations_list_url(self):
        raise NotImplementedError("Must be implemented")

    def _get_locations_url(self):
        locations_url = []
        decoded_page = self._get_decoded_source_page(
            self._get_locations_list_url())
        for match in re.finditer(self._get_location_url_pattern(), decoded_page):
            locations_url.append(match.group(Constants.LOCATION_URL_PATTERN_GROUP_NAME))
        return locations_url
