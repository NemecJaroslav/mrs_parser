import re
import requests
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from time import sleep

from production_code.common.parser import Parser
from production_code.CRS.common.constants import Constants


class CRSParser(Parser):
    def __init__(self):
        super(CRSParser, self).__init__()
        firefox_capabilities = DesiredCapabilities.FIREFOX
        firefox_capabilities['marionette'] = True
        binary = FirefoxBinary(r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe")
        self._driver = webdriver.Firefox(
            executable_path=r"C:\Users\jnemec\Documents\geckodriver-v0.26.0-win32\geckodriver.exe",
            capabilities=firefox_capabilities, firefox_binary=binary)
        self._driver.implicitly_wait(3)
        self._driver.get(self._get_locations_list_url())

    def __del__(self):
        self._driver.quit()

    def _get_decoded_source_page(self, url):
        print(url)
        self._driver.execute_script(url)
        sleep(1)
        value = self._driver.execute_script("return document.documentElement.outerHTML")
        self._driver.execute_script("window.history.back();")
        sleep(1)
        return value

    @staticmethod
    def _get_decoded_source_page_static(url):
        return requests.get(url).content.decode("latin-1")

    def _get_justified_close_locations(self):
        raise NotImplementedError("Must be implemented")

    def _get_incorrect_gps(self):
        raise NotImplementedError("Must be implemented")

    def _get_location_url_pattern(self):
        return Constants.LOCATION_URL_PATTERN

    def _get_locations_list_url(self):
        raise NotImplementedError("Must be implemented")

    def _get_location_id(self, context):
        return ""
        # return re.search(Constants.LOCATION_ID_PATTERN, context).group(
        #     Constants.LOCATION_ID_PATTERN_GROUP_NAME)

    def _get_location_name(self, context):
        return ""
        # return re.search(Constants.LOCATION_NAME_PATTERN, context).group(
        #     Constants.LOCATION_NAME_PATTERN_GROUP_NAME)

    def _get_headquarter(self, context):
        return ""
        # return re.search(Constants.HEADQUARTER_PATTERN, context).group(
        #     Constants.HEADQUARTER_PATTERN_GROUP_NAME)

    def _get_area(self, context):
        return "0,0"
        # return re.search(Constants.AREA_PATTERN, context).group(
        #     Constants.AREA_PATTERN_GROUP_NAME)

    def _get_locations_url(self):
        locations_url = []
        decoded_page = self._get_decoded_source_page_static(
            self._get_locations_list_url())
        for match in re.finditer(self._get_location_url_pattern(), decoded_page):
            locations_url.append(match.group(Constants.LOCATION_URL_PATTERN_GROUP_NAME))
        return locations_url
