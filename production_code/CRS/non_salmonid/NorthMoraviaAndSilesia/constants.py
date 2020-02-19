from production_code.common.constants import Constants


class NorthMoraviaAndSilesiaConstants(object):
    JUSTIFIED_CLOSE_LOCATIONS = []
    INCORRECT_GPS = {}
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
                             + Constants.LOCATION_NAME_PATTERN_GROUP_NAME + ">.*)[–-].*</title>")
    HEADQUARTER_PATTERN = ("<title>.*\\|.*\\|.*[–-](?P<"
                           + Constants.HEADQUARTER_PATTERN_GROUP_NAME + ">.*)</title>")
    AREA_PATTERN = ("<p><strong>(?:[\\d\\s,]*km)*\\s*(?P<"
                    + Constants.AREA_PATTERN_GROUP_NAME + ">\\d[,\\d]*)\\s*ha\\s*(?:[\\d\\s,]*km)*</strong></p>")
