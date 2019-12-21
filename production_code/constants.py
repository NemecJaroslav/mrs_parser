class Constants(object):
    MRS_HOME_PAGE = "http://www.mrsbrno.cz"
    LOCATIONS_LIST_URL = (
            MRS_HOME_PAGE
            + "/index.php/kontakty/33-seznam-reviru/"
            + "142-seznam-rybarskych-reviru-mimopstruhovych")
    LOCATION_URL_PATTERN_GROUP_NAME = "location_url"
    LOCATION_URL_PATTERN = ("(?P<"
                            + LOCATION_URL_PATTERN_GROUP_NAME
                            + ">/index.php/14-mimopstruhove-reviry/.*?)\".*?</a>")
    LOCATION_ID_PATTERN_GROUP_NAME = "location_id"
    LOCATION_ID_PATTERN = ("ev. číslo revíru:.*?(?P<"
                           + LOCATION_ID_PATTERN_GROUP_NAME
                           + ">\\d{3}\\s*\\d{3})<")
    LOCATION_NAME_PATTERN_GROUP_NAME = "location_name"
    LOCATION_NAME_PATTERN = ("<title>(?P<"
                             + LOCATION_NAME_PATTERN_GROUP_NAME
                             + ">.*?)</title>")
    HEADQUARTER_PATTERN_GROUP_NAME = "headquarter"
    HEADQUARTER_PATTERN = "hospodařením:.*?>" \
                          "(?P<" + HEADQUARTER_PATTERN_GROUP_NAME\
                          + ">[a-zA-z0-9ÁČĎÉĚÍŇÓŘŠŤÚŮÝŽáčďéěíňóřšťúůýž]" \
                          "[a-zA-z0-9ÁČĎÉĚÍŇÓŘŠŤÚŮÝŽáčďéěíňóřšťúůýž\\s.,-]+)"
    HEADQUARTER_AND_THEIR_LOCATIONS_OUTPUT = "{}, {} location(s):"
    HEADQUARTER_AND_THEIR_AREA_OUTPUT = "{}, {} ha"
    AREA_PATTERN_GROUP_NAME = "area"
    AREA_PATTERN = "výměra:.*?(?P<"\
                   + AREA_PATTERN_GROUP_NAME\
                   + ">[0-9][0-9,\\s]*)\\s+ha"
    GPS_GROUP_NAME = "gps_group"
    NON_BREAKING_SPACE = "&nbsp;"
    GPS = "\\d{1,2}\\s*[‘'°]\\s*" \
          "\\d{1,2}\\s*[‘'´]\\s*\\d{1,2}\\s*\\.?\\s*" \
          "\\d{1,3}\\s*(”|\"|''|'|´)\\s*N\\s*,*\\s*" \
          "(" + NON_BREAKING_SPACE + ")*" \
          "\\d{1,2}\\s*[‘'°]\\s*" \
          "\\d{1,2}\\s*[‘'´]\\s*\\d{1,2}\\s*\\.?\\s*" \
          "\\d{1,3}\\s*(”|\"|''|'|´)\\s*E"

    GPS_2 = "\\d{1,2}\\s*°\\s*" \
            "\\d{1,2}\\s*\\.?\\s*" \
            "\\d{1,3}\\s*(”|\"|''|'|´)\\s*N\\s*,*\\s*" \
            "(" + NON_BREAKING_SPACE + ")*" \
            "\\d{1,2}\\s*°\\s*" \
            "\\d{1,2}\\s*\\.?\\s*" \
            "\\d{1,3}\\s*(”|\"|''|'|´)\\s*E"

    GPS_3 = "\\d{1,2}\\s*[‘'°]\\s*" \
            "\\d{1,2}\\s*[‘'´]\\s*\\d{1,2}\\s*\\.?\\s*" \
            "\\d{1,3}\\s*(”|\"|''|'|´)\\s*N\\s*,*\\s*" \
            "(" + NON_BREAKING_SPACE + ")*" \
            "\\d{1,2}\\s*°\\s*" \
            "\\d{1,2}\\s*\\.?\\s*" \
            "\\d{1,3}\\s*(”|\"|''|'|´)\\s*E"

    GPS_4 = "\\d{1,2}\\s*°\\s*" \
            "\\d{1,2}\\s*\\.?\\s*" \
            "\\d{1,3}\\s*(”|\"|''|'|´)\\s*N\\s*,*\\s*" \
            "(" + NON_BREAKING_SPACE + ")*" \
            "\\d{1,2}\\s*[‘'°]\\s*" \
            "\\d{1,2}\\s*[‘'´]\\s*\\d{1,2}\\s*\\.?\\s*" \
            "\\d{1,3}\\s*(”|\"|''|'|´)\\s*E"

    GPS_PATTERNS = [
        "(?P<" + GPS_GROUP_NAME + ">" + GPS + ")",
        "(?P<" + GPS_GROUP_NAME + ">" + GPS_2 + ")",
        "(?P<" + GPS_GROUP_NAME + ">" + GPS_3 + ")",
        "(?P<" + GPS_GROUP_NAME + ">" + GPS_4 + ")",
    ]

    # TODO: incorrect GPS locations, Dyje 3A
    INCORRECT_GPS = {
        "48°45.569' N  16°52.717' E":
            "48° 45' 34.1388'' N, 16° 52' 43.0212'' E",
        "48°46.974' N  16°54.025' E":
            "48° 46' 58.44'' N, 16° 54' 1.5012'' E",
    }

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
    EXCLUDED_GPS_LOCATIONS = "The following GPS were excluded:"
    UNIQUENESS_ID_CHECK_OUTPUT = "Checking identifiers uniqueness:"
    UNIQUENESS_NAME_CHECK_OUTPUT = "Checking names uniqueness:"
    AT_LEAST_ONE_WHITE_CHARACTER = "\\s+"
    COMMA = ","
    DOT = "."
    SPACE = " "
    EMPTY_STRING = ""
    NEW_LINE = "\n"
    UTF8 = "utf-8"
