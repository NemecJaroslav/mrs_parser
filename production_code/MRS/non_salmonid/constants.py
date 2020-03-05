from production_code.common.constants import Constants
from production_code.MRS.common.constants import MRSConstants


class NonSalmonidConstants:
    LOCATIONS_LIST_URL = (
        MRSConstants.MRS_HOME_PAGE
        + "/index.php/kontakty/33-seznam-reviru/"
        + "142-seznam-rybarskych-reviru-mimopstruhovych")
    LOCATION_URL_PATTERN = ("(?P<"
                            + Constants.LOCATION_URL_PATTERN_GROUP_NAME
                            + ">/index.php/14-mimopstruhove-reviry/.*?)\".*?</a>")

    # TODO: incorrect GPS locations, Dyje 3A, Jevišovka 3A
    INCORRECT_GPS = {
        "48°45.569' N  16°52.717' E":
            "48° 45' 34.1388'' N, 16° 52' 43.0212'' E",
        "48°46.974' N  16°54.025' E":
            "48° 46' 58.44'' N, 16° 54' 1.5012'' E",
        "48.9540639N, 15.9954086E":
            "48° 57' 14.6304'' N, 15° 59' 43.4724'' E",
    }
