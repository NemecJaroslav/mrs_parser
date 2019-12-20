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
            for dms_1, dms_2 in fishing_location.gps_locations:
                dd = (self._dms_to_dd(dms_1), self._dms_to_dd(dms_2))
                distance = self._get_distance_in_km(start_point, dd)
                if (distance_limit.min_distance
                        <= distance < distance_limit.max_distance):
                    suitable_fishing_locations.append(
                        (fishing_location.identifier,
                         fishing_location.name,
                         fishing_location.headquarter,
                         dd,
                         distance))
        suitable_fishing_locations.sort(key=lambda x: x[-1])
        self._print_separated_list(suitable_fishing_locations, Constants.NEW_LINE)

    def print_all_headquarters_and_their_locations(self):
        for headquarter in sorted(
                self._headquarter_to_fishing_locations,
                key=lambda k: len(self._headquarter_to_fishing_locations[k]),
                reverse=True):
            print(Constants.HEADQUARTER_AND_THEIR_LOCATIONS_OUTPUT.format(
                headquarter,
                len(self._headquarter_to_fishing_locations[headquarter])))
            self._print_separated_list(
                [fishing_location.name
                 for fishing_location
                 in self._headquarter_to_fishing_locations[headquarter]],
                Constants.COMMA)

    def print_all_headquarters_and_their_areas(self):
        for headquarter in sorted(
                self._headquarter_to_fishing_locations,
                key=lambda k: sum([fishing_location.area
                                   for fishing_location in
                                   self._headquarter_to_fishing_locations[k]]),
                reverse=True):
            print(Constants.HEADQUARTER_AND_THEIR_AREA_OUTPUT.format(
                headquarter,
                sum([fishing_location.area
                     for fishing_location
                     in self._headquarter_to_fishing_locations[headquarter]])))

    def print_fishing_summary(self, visits):
        print("All visits: {}".format(len(visits)))
        for visit in sorted(set(visits)):
            fishing_location_name = [
                fishing_location.name for fishing_location
                in self._fishing_locations
                if (self._remove_white_characters(fishing_location.identifier)
                    == self._remove_white_characters(visit))]
            print("{} {} {}x".format(visit,
                                     fishing_location_name[0],
                                     visits.count(visit)))

    def _perform_self_check(self):
        print(Constants.UNIQUENESS_ID_CHECK_OUTPUT)
        self._verify_uniqueness(
            [item.identifier for item in self._fishing_locations])
        print(Constants.UNIQUENESS_NAME_CHECK_OUTPUT)
        self._verify_uniqueness(
            [item.name for item in self._fishing_locations])

    def _get_locations_url(self):
        locations_url = []
        decoded_page = self._get_decoded_source_page(Constants.LOCATIONS_LIST_URL)
        for match in re.finditer(Constants.LOCATION_URL_PATTERN, decoded_page):
            locations_url.append(Constants.MRS_HOME_PAGE + match.group(1))
        return locations_url

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
            print(Constants.EXCLUDED_GPS_LOCATIONS)
            MRSParser._print_separated_list(invalid_gps,
                                            Constants.NEW_LINE)
        return result

    @staticmethod
    def _dms_to_dd(dms):
        dd = (float(dms.degrees)
              + float(dms.minutes) / 60.
              + float(dms.seconds) / 3600.)
        if (dms.direction == Constants.WEST
                or dms.direction == Constants.SOUTH):
            return -dd
        return dd

    @staticmethod
    def _get_distance_in_km(location_1, location_2):
        return great_circle(location_1, location_2).km

    @staticmethod
    def _get_decoded_source_page(url):
        return requests.get(url).content.decode(Constants.UTF8)

    @staticmethod
    def _verify_uniqueness(items):
        set_items = set(items)
        if len(items) != len(set_items):
            for item in set_items:
                if items.count(item) > 1:
                    print(item)

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
                    Constants.NON_BREAKING_SPACE, Constants.SPACE)
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
        return float(MRSParser._remove_white_characters(
            MRSParser._replace_comma_with_dot(area)))

    @staticmethod
    def _replace_comma_with_dot(string):
        return re.sub(Constants.COMMA, Constants.DOT, string)

    @staticmethod
    def _remove_white_characters(string):
        return re.sub(Constants.AT_LEAST_ONE_WHITE_CHARACTER,
                      Constants.EMPTY_STRING, string)

    @staticmethod
    def _print_separated_list(li, separator):
        print(separator.join([str(item) for item in li]))
