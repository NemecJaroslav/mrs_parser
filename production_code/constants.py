class Constants(object):
    MRS_HOME_PAGE = "http://www.mrsbrno.cz"
    LOCATIONS_URL = (MRS_HOME_PAGE
                     + "/index.php/kontakty/33-seznam-reviru/"
                     + "142-seznam-rybarskych-reviru-mimopstruhovych")
    LOCATION_PATTERN = "(/index.php/14-mimopstruhove-reviry/.*?)\".*?</a>"
    LOCATION_ID_PATTERN = "ev. číslo revíru:.*?(\\d{3}\\s*\\d{3})<"
    LOCATION_NAME_PATTERN = "<title>(.*?)</title>"
    HEADQUARTER_PATTERN = "hospodařením:.*?>" \
                          "([a-zA-z0-9ÁČĎÉĚÍŇÓŘŠŤÚŮÝŽáčďéěíňóřšťúůýž]" \
                          "[a-zA-z0-9ÁČĎÉĚÍŇÓŘŠŤÚŮÝŽáčďéěíňóřšťúůýž\\s.,-]+)"
    AREA_PATTERN = "výměra:.*?([0-9][0-9,\\s]*)\\s+ha"
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
