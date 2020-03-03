from production_code.common.constants import Constants


class NorthMoraviaAndSilesiaConstants(object):
    JUSTIFIED_CLOSE_LOCATIONS = []
    INCORRECT_GPS = {
        "49.5862275N, 17.2619967E":
            "49° 35' 10.4172'' N, 17° 15' 43.1892'' E",
        "49.5634489N, 17.2652725E":
            "49° 33' 48.4164'' N, 17° 15' 54.9792'' E",
    }
    LOCATIONS_PER_PAGE = [
        "https://www.rybsvaz-ms.cz/katalog/rybarske-reviry/mimopstruhove-reviry/filtrovani-polozek.php?recordStart=0",
        "https://www.rybsvaz-ms.cz/katalog/rybarske-reviry/mimopstruhove-reviry/filtrovani-polozek.php?recordStart=20",
        "https://www.rybsvaz-ms.cz/katalog/rybarske-reviry/mimopstruhove-reviry/filtrovani-polozek.php?recordStart=40",
        "https://www.rybsvaz-ms.cz/katalog/rybarske-reviry/mimopstruhove-reviry/filtrovani-polozek.php?recordStart=60",
        "https://www.rybsvaz-ms.cz/katalog/rybarske-reviry/mimopstruhove-reviry/filtrovani-polozek.php?recordStart=80",
        "https://www.rybsvaz-ms.cz/katalog/rybarske-reviry/mimopstruhove-reviry/filtrovani-polozek.php?recordStart=100",
        "https://www.rybsvaz-ms.cz/katalog/rybarske-reviry/mimopstruhove-reviry/filtrovani-polozek.php?recordStart=120",
        "https://www.rybsvaz-ms.cz/katalog/rybarske-reviry/mimopstruhove-reviry/filtrovani-polozek.php?recordStart=140",
        "https://www.rybsvaz-ms.cz/katalog/rybarske-reviry/mimopstruhove-reviry/filtrovani-polozek.php?recordStart=160",
        "https://www.rybsvaz-ms.cz/katalog/rybarske-reviry/mimopstruhove-reviry/filtrovani-polozek.php?recordStart=174",
    ]
    LOCATION_URL_PATTERN = ("<a href=\"(?P<"
                            + Constants.LOCATION_URL_PATTERN_GROUP_NAME
                            + ">/katalog/rybarske-reviry/mimopstruhove-reviry/.*.html)\"")
    NORTHMORAVIAANDSILESIA_HOME_PAGE = "https://www.rybsvaz-ms.cz"
    LOCATION_ID_PATTERN = "(?P<" + Constants.LOCATION_ID_PATTERN_GROUP_NAME + ">47\\d\\s*\\d{3})"
    LOCATION_NAME_PATTERN = ("<title>.*\\|.*\\|" + "(?P<"
                             + Constants.LOCATION_NAME_PATTERN_GROUP_NAME + ">.*)[–-].*MO.*</title>")
    HEADQUARTER_PATTERN = ("<title>.*\\|.*\\|.*[–-](?P<"
                           + Constants.HEADQUARTER_PATTERN_GROUP_NAME + ">.*MO.*)</title>")
    AREA_PATTERN = ("<p><strong>(?:[\\d\\s,]*km)*\\s*(?P<"
                    + Constants.AREA_PATTERN_GROUP_NAME + ">\\d[,\\d]*)\\s*ha\\s*(?:[\\d\\s,]*km)*</strong></p>")
