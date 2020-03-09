class Constants:
    LOCATION_URL_PATTERN_GROUP_NAME = "location_url"
    LOCATION_ID_PATTERN_GROUP_NAME = "location_id"
    LOCATION_NAME_PATTERN_GROUP_NAME = "location_name"
    HEADQUARTER_PATTERN_GROUP_NAME = "headquarter"
    AREA_PATTERN_GROUP_NAME = "area"
    HEADQUARTER_AND_THEIR_LOCATIONS_OUTPUT = "{}, {} location(s):"
    HEADQUARTER_AND_THEIR_AREA_OUTPUT = "{}, {} ha"
    GPS_GROUP_NAME = "gps_group"
    NON_BREAKING_SPACE = "&nbsp;"
    GPS = "[\\d°”‘´'\".\\s,“]+N[\\s,&nbsp;]*[\\d°\"‘”´'.\\s,“]+E"
    GPS_PATTERNS = [
        "(?P<" + GPS_GROUP_NAME + ">" + GPS + ")"
    ]

    NUMBERS_PATTERN = "\\d+\\.*\\d*"
    NORTH = "N"
    SOUTH = "S"
    WEST = "W"
    EAST = "E"
    DIRECTIONS_PATTERN = ("["
                          + NORTH
                          + SOUTH
                          + WEST
                          + EAST
                          + "]")
    MINUTES_IN_HOUR = 60
    SECONDS_IN_HOUR = 3600
    EXCLUDED_GPS_LOCATIONS = "The following GPS were excluded:"
    NUMBERS_IN_DMS_FORMAT = 6
    DIRECTIONS_IN_DMS_FORMAT = 2
    UNIQUENESS_OCCURRENCE_COUNT = 1
    UNIQUENESS_ID_CHECK_OUTPUT = "Checking identifiers uniqueness:"
    UNIQUENESS_NAME_CHECK_OUTPUT = "Checking names uniqueness:"
    SUITABLE_FISHING_LOCATION = "suitable_fishing_location"
    SUITABLE_FISHING_LOCATION_MEMBERS = "id name headquarter gps distance"
    SUSPICIOUSLY_CLOSE_GPS_LOCATION = "suspiciously_close_gps_location"
    SUSPICIOUSLY_CLOSE_GPS_LOCATION_MEMBERS = "location_1 location_2 gps_1 gps_2 distance"
    HEADQUARTERS_LOCATIONS_DISTANCE = "headquarters_locations_distance"
    HEADQUARTERS_LOCATIONS_DISTANCE_MEMBERS = "headquarter name gps distance"
    FISHING_SUMMARY_TOTAL_VISITS_COUNT_OUTPUT = "Total visits count = {}"
    FISHING_SUMMARY_TRANSLATION_ERROR = "ERROR"
    AT_LEAST_ONE_WHITE_CHARACTER = "\\s+"
    COMMA = ","
    COMMA_IN_NUMBER = r"(\d+)(,)(\d+)"
    DOT = "."
    DOT_IN_NUMBER = r"\1.\3"
    SPACE = " "
    EMPTY_STRING = ""
    NEW_LINE = "\n"
    TIMES = "x"
    UTF8 = "utf-8"
    EMPTY_AREA = "0,0"
    EMPTY_AREA_WARNING = "No area found."
