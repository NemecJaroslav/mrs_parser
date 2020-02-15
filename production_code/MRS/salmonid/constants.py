from production_code.common.constants import Constants


class SalmonidConstants(object):
    LOCATIONS_LIST_URL = (
            Constants.MRS_HOME_PAGE
            + "/index.php/kontakty/33-seznam-reviru/"
            + "143-seznam-rybarskych-reviru-pstruhovych")
    LOCATION_URL_PATTERN = ("(?P<"
                            + Constants.LOCATION_URL_PATTERN_GROUP_NAME
                            + ">/index.php/15-pstruhove-reviry/.*?)\".*?</a>")

    INCORRECT_GPS = {}
