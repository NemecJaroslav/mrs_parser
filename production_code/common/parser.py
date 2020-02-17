import re
import requests
import itertools
from collections import defaultdict, namedtuple
from geopy.distance import great_circle

from production_code.common.constants import Constants
from production_code.common.gps_coordinate import GPSCoordinate
from production_code.common.fishing_location import FishingLocation
from production_code.common.fishing_summary import FishingSummary


class Parser(object):
    suitable_fishing_location = namedtuple(
        Constants.SUITABLE_FISHING_LOCATION,
        Constants.SUITABLE_FISHING_LOCATION_MEMBERS)

    suspiciously_close_gps_location = namedtuple(
        Constants.SUSPICIOUSLY_CLOSE_GPS_LOCATION,
        Constants.SUSPICIOUSLY_CLOSE_GPS_LOCATION_MEMBERS
    )

    def __init__(self):
        self._fishing_locations = []
        self._headquarter_to_fishing_locations = defaultdict(list)

    def parse(self):
        for location_url in self._get_locations_url():
            decoded_page = self._get_decoded_source_page(location_url)
            fishing_location = FishingLocation(
                self._remove_white_characters(self._get_location_id(decoded_page)),
                self._get_location_name(decoded_page).strip().upper(),
                self._get_headquarter(decoded_page).strip().upper(),
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
                        self.suitable_fishing_location(
                            fishing_location.identifier,
                            fishing_location.name,
                            fishing_location.headquarter,
                            dd,
                            distance)
                        )
        suitable_fishing_locations.sort(key=lambda x: x.distance)
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

    def print_fishing_summary_given_by_id(self, visits):
        visits = [self._remove_white_characters(visit) for visit in visits]
        self._print_fishing_summary(
            [FishingSummary(visit,
                            None,
                            visits.count(visit))
             for visit in set(visits)], len(visits))

    def print_fishing_summary_given_by_name(self, visits):
        visits = [visit.strip().upper() for visit in visits]
        self._print_fishing_summary(
            [FishingSummary(None,
                            visit,
                            visits.count(visit))
             for visit in set(visits)], len(visits))

    def print_suspiciously_close_gps_locations(self, distance_limit):
        suspiciously_close_gps_locations = (self._get_suspiciously_close_gps_locations_within_one_fishing_location(
            distance_limit) + self._get_suspiciously_close_gps_locations_between_different_fishing_locations(
            distance_limit))
        suspiciously_close_gps_locations.sort(key=lambda x: x.distance)
        self._print_separated_list(suspiciously_close_gps_locations, Constants.NEW_LINE)

    def _get_justified_close_locations(self):
        raise NotImplementedError("Must be implemented")

    def _get_suspiciously_close_gps_locations_within_one_fishing_location(self, distance_limit):
        suspiciously_close_gps_locations = []
        for fishing_location in self._fishing_locations:
            for gps_1, gps_2 in itertools.combinations(fishing_location.gps_locations, 2):
                gps_1_dms_1, gps_1_dms_2 = gps_1
                gps_2_dms_1, gps_2_dms_2 = gps_2
                gps_1_dd = (self._dms_to_dd(gps_1_dms_1), self._dms_to_dd(gps_1_dms_2))
                gps_2_dd = (self._dms_to_dd(gps_2_dms_1), self._dms_to_dd(gps_2_dms_2))
                distance = self._get_distance_in_km(gps_1_dd, gps_2_dd)
                if ((distance_limit.min_distance
                     <= distance <= distance_limit.max_distance)
                        and not (gps_1_dd, gps_2_dd) in self._get_justified_close_locations()):
                    suspiciously_close_gps_locations.append(self.suspiciously_close_gps_location(fishing_location.name,
                                                                                                 fishing_location.name,
                                                                                                 gps_1_dd, gps_2_dd,
                                                                                                 distance))
        return suspiciously_close_gps_locations

    def _get_suspiciously_close_gps_locations_between_different_fishing_locations(self, distance_limit):
        suspiciously_close_gps_locations = []
        for fishing_location_1, fishing_location_2 in itertools.combinations(self._fishing_locations, 2):
            for gps_1, gps_2 in itertools.product(fishing_location_1.gps_locations, fishing_location_2.gps_locations):
                gps_1_dms_1, gps_1_dms_2 = gps_1
                gps_2_dms_1, gps_2_dms_2 = gps_2
                gps_1_dd = (self._dms_to_dd(gps_1_dms_1), self._dms_to_dd(gps_1_dms_2))
                gps_2_dd = (self._dms_to_dd(gps_2_dms_1), self._dms_to_dd(gps_2_dms_2))
                distance = self._get_distance_in_km(gps_1_dd, gps_2_dd)
                if ((distance_limit.min_distance
                     <= distance <= distance_limit.max_distance)
                        and not (gps_1_dd, gps_2_dd) in self._get_justified_close_locations()):
                    suspiciously_close_gps_locations.append(self.suspiciously_close_gps_location(
                        fishing_location_1.name, fishing_location_2.name, gps_1_dd, gps_2_dd, distance))
        return suspiciously_close_gps_locations

    def _print_fishing_summary(self, fishing_summary, total_visits_count):
        print(Constants.FISHING_SUMMARY_TOTAL_VISITS_COUNT_OUTPUT.format(
            total_visits_count))
        for record in fishing_summary:
            if record.name is None:
                record.name = self._identifier_to_name(record.identifier)
            elif record.identifier is None:
                record.identifier = self._name_to_identifier(record.name)
        fishing_summary.sort(key=lambda x: x.identifier)
        self._print_separated_list(fishing_summary, Constants.NEW_LINE)

    def _identifier_to_name(self, identifier):
        return next(iter([fishing_location.name for fishing_location
                          in self._fishing_locations
                          if fishing_location.identifier == identifier]),
                    Constants.FISHING_SUMMARY_TRANSLATION_ERROR)

    def _name_to_identifier(self, name):
        return next(iter([fishing_location.identifier for fishing_location
                          in self._fishing_locations
                          if fishing_location.name == name]),
                    Constants.FISHING_SUMMARY_TRANSLATION_ERROR)

    def _perform_self_check(self):
        print(Constants.UNIQUENESS_ID_CHECK_OUTPUT)
        self._verify_uniqueness(
            [item.identifier for item in self._fishing_locations])
        print(Constants.UNIQUENESS_NAME_CHECK_OUTPUT)
        self._verify_uniqueness(
            [item.name for item in self._fishing_locations])

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

    def _get_incorrect_gps(self):
        raise NotImplementedError("Must be implemented")

    def _convert_string_to_gps(self, gps_strings):
        result = []
        invalid_gps = []
        for gps_string in gps_strings:

            incorrect_gps = self._get_incorrect_gps()

            if gps_string in incorrect_gps:
                gps_string = incorrect_gps[gps_string]

            numbers = re.findall(Constants.NUMBERS_PATTERN, gps_string)
            directions = re.findall(Constants.DIRECTIONS_PATTERN, gps_string)
            if (len(numbers) != Constants.NUMBERS_IN_DMS_FORMAT
                    or len(directions) != Constants.DIRECTIONS_IN_DMS_FORMAT):
                invalid_gps.append(gps_string)
                continue
            degrees_1, minutes_1, seconds_1, degrees_2, minutes_2, seconds_2 = map(float, numbers)
            direction_1, direction_2 = directions
            first_coord = GPSCoordinate(degrees_1, minutes_1, seconds_1, direction_1)
            second_coord = GPSCoordinate(degrees_2, minutes_2, seconds_2, direction_2)
            result.append((first_coord, second_coord))
        if invalid_gps:
            print(Constants.EXCLUDED_GPS_LOCATIONS)
            Parser._print_separated_list(invalid_gps,
                                         Constants.NEW_LINE)
        return result

    @staticmethod
    def _dms_to_dd(dms):
        dd = (dms.degrees
              + dms.minutes / Constants.MINUTES_IN_HOUR
              + dms.seconds / Constants.SECONDS_IN_HOUR)
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
                if items.count(item) > Constants.UNIQUENESS_OCCURRENCE_COUNT:
                    print(item + Constants.SPACE + str(items.count(item)) + Constants.TIMES)

    @staticmethod
    def _get_location_id(context):
        return re.search(Constants.LOCATION_ID_PATTERN, context).group(
            Constants.LOCATION_ID_PATTERN_GROUP_NAME)

    @staticmethod
    def _get_location_name(context):
        return re.search(Constants.LOCATION_NAME_PATTERN, context).group(
            Constants.LOCATION_NAME_PATTERN_GROUP_NAME)

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
        return re.search(Constants.HEADQUARTER_PATTERN, context).group(
            Constants.HEADQUARTER_PATTERN_GROUP_NAME)

    @staticmethod
    def _get_area(context):
        return re.search(Constants.AREA_PATTERN, context).group(
            Constants.AREA_PATTERN_GROUP_NAME)

    @staticmethod
    def _string_area_to_float(area):
        return float(Parser._remove_white_characters(
            Parser._replace_comma_with_dot(area)))

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
