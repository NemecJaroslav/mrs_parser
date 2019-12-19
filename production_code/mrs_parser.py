import re
import requests
from collections import defaultdict
from geopy.distance import great_circle

from .constants import Constants
from .gps_coordinate import GPSCoordinate
from .fishing_location import FishingLocation


class MRSParser(object):
    def __init__(self):
        self._fishing_locations = []
        self._headquarter_to_fishing_locations = defaultdict(list)

    def parse(self):
        for location_url in self._get_locations_url():
            decoded_page = self._get_decoded_source_page(location_url)
            fishing_location = FishingLocation(
                self._get_location_id(decoded_page),
                self._get_location_name(decoded_page),
                self._get_headquarter(decoded_page),
                self._string_area_to_float(self._get_area(decoded_page)),
                self._convert_string_to_gps(self._get_gps(decoded_page))
            )
            self._fishing_locations.append(fishing_location)
            self._headquarter_to_fishing_locations[fishing_location.headquarter].append(fishing_location)
        self._perform_self_check()

    def print_suitable_fishing_locations(self, start_point, distance_limit):
        suitable_fishing_locations = []
        for fishing_location in self._fishing_locations:
            for location in fishing_location.gps_locations:
                dd_1 = self._dms_to_dd(location[0].degrees,
                                       location[0].minutes,
                                       location[0].seconds,
                                       location[0].direction)
                dd_2 = self._dms_to_dd(location[1].degrees,
                                       location[1].minutes,
                                       location[1].seconds,
                                       location[1].direction)
                distance = self._get_distance_in_km(start_point, (dd_1, dd_2))
                if distance_limit[0] <= distance < distance_limit[1]:
                    suitable_fishing_locations.append(
                        (fishing_location.identifier,
                         fishing_location.name,
                         fishing_location.headquarter,
                         (dd_1, dd_2),
                         distance))
        suitable_fishing_locations.sort(key=lambda x: x[-1])
        for suitable_fishing_location in suitable_fishing_locations:
            print(suitable_fishing_location)

    def print_all_headquarters_and_their_locations(self):
        for headquarter in sorted(self._headquarter_to_fishing_locations,
                                  key=lambda k: len(self._headquarter_to_fishing_locations[k]),
                                  reverse=True):
            print("{}, {} location(s)".format(
                headquarter,
                len(self._headquarter_to_fishing_locations[
                        headquarter])), end=":\n")
            for fishing_location in self._headquarter_to_fishing_locations[headquarter]:
                print(fishing_location.name, end=", ")
            print(end="\n")

    def print_all_headquarters_and_their_areas(self):
        for headquarter in sorted(self._headquarter_to_fishing_locations,
                                  key=lambda k: sum([fishing_location.area
                                                     for fishing_location in
                                                     self._headquarter_to_fishing_locations[k]]),
                                  reverse=True):
            print("{}, {} ha".format(headquarter, sum([fishing_location.area
                                                       for fishing_location in
                                                       self._headquarter_to_fishing_locations[headquarter]])))

    @staticmethod
    def _convert_string_to_gps(gps_strings):
        result = []
        invalid_gps = []
        for gps_string in gps_strings:

            if gps_string in Constants.INCORRECT_GPS:
                gps_string = Constants.INCORRECT_GPS[gps_string]

            numbers = re.findall(Constants.NUMBERS_PATTERN, gps_string)
            directions = re.findall(Constants.DIRECTIONS_PATTERN, gps_string)
            if len(numbers) != 6 or len(directions) != 2:
                invalid_gps.append(gps_string)
                continue
            first_coord = GPSCoordinate(float(numbers[0]),
                                        float(numbers[1]),
                                        float(numbers[2]),
                                        directions[0])
            second_coord = GPSCoordinate(float(numbers[3]),
                                         float(numbers[4]),
                                         float(numbers[5]),
                                         directions[1])
            result.append((first_coord, second_coord))
        if invalid_gps:
            print("The following GPS were excluded:")
            for _ in invalid_gps:
                print(_)
        return result

    @staticmethod
    def _dms_to_dd(degree, minutes, seconds, direction):
        dd = float(degree) + float(minutes) / 60. + float(seconds) / 3600.
        if (direction == Constants.WEST
                or direction == Constants.SOUTH):
            return -dd
        return dd

    @staticmethod
    def _get_distance_in_km(location_1, location_2):
        return great_circle(location_1, location_2).km

    @staticmethod
    def _get_decoded_source_page(url):
        page = requests.get(url)
        return page.content.decode('utf-8')

    @staticmethod
    def _verify_uniqueness(items):
        set_items = set(items)
        if len(items) != len(set_items):
            for item in set_items:
                if items.count(item) > 1:
                    print(item)

    def _perform_self_check(self):
        print("Checking identifiers uniqueness:")
        self._verify_uniqueness(
            [item.identifier for item in self._fishing_locations])
        print("Checking names uniqueness:")
        self._verify_uniqueness(
            [item.name for item in self._fishing_locations])
        print("Done")

    def _get_locations_url(self):
        locations_url = []
        decoded_page = self._get_decoded_source_page(Constants.LOCATIONS_LIST_URL)
        for match in re.finditer(Constants.LOCATION_URL_PATTERN, decoded_page):
            locations_url.append(Constants.MRS_HOME_PAGE + match.group(1))
        return locations_url

    @staticmethod
    def _get_location_id(context):
        return re.search(Constants.LOCATION_ID_PATTERN, context).group(1)

    @staticmethod
    def _get_location_name(context):
        return re.search(Constants.LOCATION_NAME_PATTERN, context).group(1)

    @staticmethod
    def _get_gps(context):
        gps = []
        for gps_pattern in Constants.GPS_PATTERNS:
            for match in re.finditer(gps_pattern, context):
                current_gps = match.group(Constants.GPS_GROUP_NAME).replace(
                    Constants.NON_BREAKING_SPACE, " ")
                gps.append(current_gps)
        return gps

    @staticmethod
    def _get_headquarter(context):
        return re.search(Constants.HEADQUARTER_PATTERN, context).group(1)

    @staticmethod
    def _get_area(context):
        return re.search(Constants.AREA_PATTERN, context).group(1)

    @staticmethod
    def _string_area_to_float(area):
        return float(re.sub(r"\s+", "", re.sub(r",", ".", area)))
