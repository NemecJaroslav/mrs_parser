from production_code.common.constants import Constants


class NorthMoraviaAndSilesiaCommonConstants:
    NORTHMORAVIAANDSILESIA_HOME_PAGE = "https://www.rybsvaz-ms.cz"
    LOCATION_ID_PATTERN = "<strong>\\s*(?P<" + Constants.LOCATION_ID_PATTERN_GROUP_NAME + ">47\\d\\s*\\d{3})"
    LOCATION_NAME_PATTERN = ("<title>.*\\|.*\\|" + "(?P<"
                             + Constants.LOCATION_NAME_PATTERN_GROUP_NAME
                             + ">.*)[–-].*(MO|VÚS|ÚS).*</title>")
    HEADQUARTER_PATTERN = ("<title>.*\\|.*\\|.*[–-](?P<"
                           + Constants.HEADQUARTER_PATTERN_GROUP_NAME + ">.*(MO|VÚS|ÚS).*)</title>")
    AREA_PATTERN = ("<p><strong>(?:[\\d\\s,]*km)*\\s*(?P<"
                    + Constants.AREA_PATTERN_GROUP_NAME
                    + ">\\d[,\\d]*)\\s*ha\\s*(?:[\\d\\s,]*km)*</strong></p>")
