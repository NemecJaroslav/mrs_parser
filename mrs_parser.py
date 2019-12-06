import re
import requests
from geopy.distance import great_circle


class GPSCoordinate(object):
    def __init__(self, degrees, minutes, seconds, direction):
        self.degrees = degrees
        self.minutes = minutes
        self.seconds = seconds
        self.direction = direction

    def __eq__(self, other):
        if isinstance(other, GPSCoordinate):
            return (self.degrees == other.degrees
                    and self.minutes == other.minutes
                    and self.seconds == other.seconds
                    and self.direction == other.direction)
        return False

    def __str__(self):
        return (str(self.degrees)
                + "," + str(self.minutes)
                + "," + str(self.seconds)
                + "," + self.direction)


class FishingLocation(object):
    def __init__(self, identifier, name, locations):
        self.identifier = identifier
        self.name = name
        self.locations = locations

    def __str__(self):
        return self.identifier + ", " + self.name


class MRSParser(object):
    def __init__(self):
        self._fishing_locations = []
        self._mrs_home_page = "http://www.mrsbrno.cz"
        self._locations_url = (self._mrs_home_page
                               + "/index.php/kontakty/33-seznam-reviru/"
                               + "142-seznam-rybarskych-reviru-mimopstruhovych")
        self._location_pattern = "(/index.php/14-mimopstruhove-reviry/.*?)\".*?</a>"
        self._location_id_pattern = "ev. číslo revíru:.*?(\\d{3}\\s*\\d{3})<"
        self._location_name_pattern = "<title>(.*?)</title>"
        self._gps_group_name = "gps_group"
        self._gps = "\\d{1,2}\\s*[‘'°]\\s*" \
                    "\\d{1,2}\\s*[‘'´]\\s*\\d{1,2}\\s*\\.?\\s*" \
                    "\\d{1,3}\\s*(”|\"|''|'|´)\\s*N\\s*,*\\s*" \
                    "(&nbsp;)*" \
                    "\\d{1,2}\\s*[‘'°]\\s*" \
                    "\\d{1,2}\\s*[‘'´]\\s*\\d{1,2}\\s*\\.?\\s*" \
                    "\\d{1,3}\\s*(”|\"|''|'|´)\\s*E"
        self._gps_2 = "\\d{1,2}\\s*°\\s*" \
                      "\\d{1,2}\\s*\\.?\\s*" \
                      "\\d{1,3}\\s*(”|\"|''|'|´)\\s*N\\s*,*\\s*" \
                      "(&nbsp;)*" \
                      "\\d{1,2}\\s*°\\s*" \
                      "\\d{1,2}\\s*\\.?\\s*" \
                      "\\d{1,3}\\s*(”|\"|''|'|´)\\s*E"
        self._gps_3 = "\\d{1,2}\\s*[‘'°]\\s*" \
                      "\\d{1,2}\\s*[‘'´]\\s*\\d{1,2}\\s*\\.?\\s*" \
                      "\\d{1,3}\\s*(”|\"|''|'|´)\\s*N\\s*,*\\s*" \
                      "(&nbsp;)*" \
                      "\\d{1,2}\\s*°\\s*" \
                      "\\d{1,2}\\s*\\.?\\s*" \
                      "\\d{1,3}\\s*(”|\"|''|'|´)\\s*E"
        self._gps_4 = "\\d{1,2}\\s*°\\s*" \
                      "\\d{1,2}\\s*\\.?\\s*" \
                      "\\d{1,3}\\s*(”|\"|''|'|´)\\s*N\\s*,*\\s*" \
                      "(&nbsp;)*" \
                      "\\d{1,2}\\s*[‘'°]\\s*" \
                      "\\d{1,2}\\s*[‘'´]\\s*\\d{1,2}\\s*\\.?\\s*" \
                      "\\d{1,3}\\s*(”|\"|''|'|´)\\s*E"
        self._gps_pattern = "(?P<" + self._gps_group_name + ">" + self._gps + ")"
        self._gps_pattern_2 = "(?P<" + self._gps_group_name + ">" + self._gps_2 + ")"
        self._gps_pattern_3 = "(?P<" + self._gps_group_name + ">" + self._gps_3 + ")"
        self._gps_pattern_4 = "(?P<" + self._gps_group_name + ">" + self._gps_4 + ")"

    def parse(self):
        locations = self._get_locations()
        for location in locations:
            decoded_content = self._get_decoded_source_page(location)
            self._fishing_locations.append(
                FishingLocation(self._get_location_id(decoded_content),
                                self._get_location_name(decoded_content),
                                self._convert_string_to_gps(self._get_gps(decoded_content))))
        self._perform_self_check()

    def get_suitable_fishing_locations(self, start_point, distance_limit):
        result = []
        for fishing_location in self._fishing_locations:
            for location in fishing_location.locations:
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
                    result.append((fishing_location.identifier,
                                   fishing_location.name,
                                   (dd_1, dd_2),
                                   distance))
        result.sort(key=lambda x: x[-1])
        return result

    @staticmethod
    def _convert_string_to_gps(gps_strings):
        result = []
        invalid_gps = []
        for gps_string in gps_strings:

            # TODO: two incorrect GPS locations, Dyje 3A
            if gps_string == "48°45.569' N  16°52.717' E":
                gps_string = "48° 45' 34.1388'' N, 16° 52' 43.0212'' E"
            elif gps_string == "48°46.974' N  16°54.025' E":
                gps_string = "48° 46' 58.44'' N, 16° 54' 1.5012'' E"

            numbers = re.findall("\\d+\\.*\\d*", gps_string)
            directions = re.findall("[NEWS]", gps_string)
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
        if direction == 'W' or direction == 'S':
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

    def _get_locations(self):
        locations = []
        decoded_content = self._get_decoded_source_page(self._locations_url)
        for match in re.finditer(self._location_pattern, decoded_content):
            locations.append(self._mrs_home_page + match.group(1))
        return locations

    def _get_location_id(self, context):
        return re.search(self._location_id_pattern, context).group(1)

    def _get_location_name(self, context):
        return re.search(self._location_name_pattern, context).group(1)

    def _get_gps(self, context):
        gps = []
        for gps_pattern in [self._gps_pattern,
                            self._gps_pattern_2,
                            self._gps_pattern_3,
                            self._gps_pattern_4
                            ]:
            for match in re.finditer(gps_pattern, context):
                current_gps = match.group(self._gps_group_name).replace(
                    "&nbsp;", " ")
                gps.append(current_gps)
        return gps
