import re
import requests
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from time import sleep

from production_code.common.parser import Parser
from production_code.CRS.common.constants import Constants


class CRSParser(Parser):
    def _get_decoded_source_page(self, url):
        firefox_capabilities = DesiredCapabilities.FIREFOX
        firefox_capabilities['marionette'] = True
        binary = FirefoxBinary(r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe")
        driver = webdriver.Firefox(
            executable_path=r"C:\Users\jnemec\Documents\geckodriver-v0.26.0-win32\geckodriver.exe",
            capabilities=firefox_capabilities, firefox_binary=binary)
        driver.implicitly_wait(3)
        driver.get(self._get_locations_list_url())
        driver.execute_script(url)
        sleep(0.1)
        value = driver.execute_script("return document.documentElement.outerHTML")
        driver.quit()
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

    def _get_locations_url(self):
        locations_url = []
        decoded_page = self._get_decoded_source_page_static(
            self._get_locations_list_url())
        for match in re.finditer(self._get_location_url_pattern(), decoded_page):
            locations_url.append(match.group(Constants.LOCATION_URL_PATTERN_GROUP_NAME))
        return locations_url
