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
    LOCATION_ID_PATTERN = "(?P<" + Constants.LOCATION_ID_PATTERN_GROUP_NAME + ">471\\s*\\d{3})"
