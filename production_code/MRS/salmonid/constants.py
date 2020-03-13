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
    HEADQUARTER_GPS = {
        "BOSKOVICE": (49.4908731, 16.6943608),
        "TIŠNOV": (49.3425425, 16.4272783),
        "BLANSKO": (49.3646939, 16.6370919),
        "VEVERSKÁ BÍTÝŠKA": (49.2782894, 16.4363511),
        "VELKÁ BÍTEŠ": (49.2886492, 16.2269047),
        "UHERSKÝ BROD": (49.0305231, 17.6331086),
        "UHERSKÉ HRADIŠTĚ": (49.0739647, 17.4734000),
        "BYSTŘICE POD HOSTÝNEM": (49.3999906, 17.6720375),
        "BYSTŘICE NAD PERNŠTEJNEM": (49.5224858, 16.2548258),
        "ŽĎÁR NAD SÁZAVOU": (49.5610386, 15.9283689),
        "ZLÍN": (49.2261231, 17.6843786),
        "ZNOJMO": (48.8367225, 16.0680575),
        "VRANOV NAD DYJÍ": (48.9088139, 15.7882208),
        "TELČ": (49.1799347, 15.4641053),
        "NOVÉ MĚSTO NA MORAVĚ": (49.5726742, 16.0708633),
        "VYŠKOV": (49.2779142, 17.0014172),
        "PROSTĚJOV": (49.4703175, 17.1040044),
        "NEDVĚDICE": (49.5041311, 16.3387117),
        "NÁMĚŠŤ NAD OSLAVOU": (49.2084344, 16.1613239),
        "IVANČICE": (49.1063772, 16.3662583),
        "NOVÁ VES U OSLAVAN": (49.1062867, 16.3149697),
        "MOHELNO": (49.1139642, 16.1907844),
        "TŘEBÍČ": (49.2165169, 15.8570558),
        "SLAVIČÍN": (49.0871503, 17.8796653),
        "KROMĚŘÍŽ": (49.2991753, 17.3865678),
        "LETOVICE": (49.5479219, 16.5691097),
        "ADAMOV": (49.3023733, 16.6498875),
        "OSVĚTIMANY": (49.0561333, 17.2498797),
        "DOLNÍ LOUČKY": (49.3612850, 16.3509867),
        "BRNO 4": (49.2054592, 16.7061336),
        "DOLNÍ ROŽÍNKA": (49.4748303, 16.2063069),
        "JIHLAVA": (49.4091378, 15.5934542),
        "HOLEŠOV": (49.3333517, 17.5781622),
    }
