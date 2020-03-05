from production_code.common.constants import Constants
from production_code.MRS.common.constants import MRSConstants


class SalmonidConstants:
    LOCATIONS_LIST_URL = (
        MRSConstants.MRS_HOME_PAGE
        + "/index.php/kontakty/33-seznam-reviru/"
        + "143-seznam-rybarskych-reviru-pstruhovych")
    LOCATION_URL_PATTERN = ("(?P<"
                            + Constants.LOCATION_URL_PATTERN_GROUP_NAME
                            + ">/index.php/15-pstruhove-reviry/.*?)\".*?</a>")

    INCORRECT_GPS = {}
