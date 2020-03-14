from production_code.common.constants import Constants


class NorthMoraviaAndSilesiaSalmonidConstants:
    JUSTIFIED_CLOSE_LOCATIONS = []
    LOCATIONS_PER_PAGE = [
        "https://www.rybsvaz-ms.cz/katalog/rybarske-reviry/pstruhove-reviry/filtrovani-polozek.php?recordStart=0",
        "https://www.rybsvaz-ms.cz/katalog/rybarske-reviry/pstruhove-reviry/filtrovani-polozek.php?recordStart=20",
        "https://www.rybsvaz-ms.cz/katalog/rybarske-reviry/pstruhove-reviry/filtrovani-polozek.php?recordStart=40",
        "https://www.rybsvaz-ms.cz/katalog/rybarske-reviry/pstruhove-reviry/filtrovani-polozek.php?recordStart=60",
        "https://www.rybsvaz-ms.cz/katalog/rybarske-reviry/pstruhove-reviry/filtrovani-polozek.php?recordStart=80",
        "https://www.rybsvaz-ms.cz/katalog/rybarske-reviry/pstruhove-reviry/filtrovani-polozek.php?recordStart=100",
    ]
    LOCATION_URL_PATTERN = ("<a href=\"(?P<"
                            + Constants.LOCATION_URL_PATTERN_GROUP_NAME
                            + ">/katalog/rybarske-reviry/pstruhove-reviry/.*.html)\"")

    INCORRECT_GPS = {
        # LUBINA 3
        "49°33‘0.013“N,\n18°171‘1.240“E":
            "49°33'0.041\"N, 18°9'36.622\"E"
    }
    HEADQUARTER_GPS = {
        "MO VALAŠSKÉ MEZIŘÍČÍ": (49.4575567, 17.9869111),
        "MO ROŽNOV POD RADHOŠTĚM": (49.4615447, 18.1425514),
        "MO VSETÍN": (49.3337506, 17.9884611),
        "MO JESENÍK": (50.2177300, 17.2070522),
        "MO BÍLOVEC": (49.7598675, 18.0203961),
        "MO ŠUMPERK": (49.9668033, 16.9747031),
        "MO ZÁBŘEH NA MORAVĚ": (49.8780325, 16.8717022),
        "MO VÍTKOV": (49.7749544, 17.7501242),
        "MO VELKÁ BYSTŘICE": (49.5931169, 17.3467811),
        "MO DOMAŠOV NAD BYSTŘICÍ": (49.7421519, 17.4451853),
        "MO FRÝDLANT NAD OSTRAVICÍ": (49.5654200, 18.3505125),
        "MO VRBNO POD PRADĚDEM": (50.1218706, 17.3740400),
        "MO BRUNTÁL": (49.9733703, 17.4728339),
        "MO JAVORNÍK": (50.3923175, 17.0079122),
        "MO OPAVA": (49.9366425, 17.9179214),
        "MO BYSTŘICE NAD OLŠÍ": (49.6367725, 18.7208733),
        "MO KRNOV": (50.0868806, 17.7093039),
        "MO FULNEK": (49.7159878, 17.9070500),
        "MO NOVÝ JIČÍN": (49.5938208, 18.0121372),
        "MO CHORYNĚ": (49.4965175, 17.8968361),
        "MO KELČ": (49.4762997, 17.8182542),
        "MO PŘÍBOR": (49.6418581, 18.1490892),
        "MO RÝMAŘOV": (49.9316686, 17.2637747),
        "MO LIPNÍK NAD BEČVOU": (49.5249303, 17.5878428),
        "MO UNIČOV": (49.7721319, 17.1204328),
        "MO JABLUNKOV": (49.5844753, 18.7788103),
        "MO FRENŠTÁT POD RADHOŠTĚM": (49.5496131, 18.2051661),
        "MO HAVÍŘOV": (49.7710231, 18.5060006),
        "MO LUČINA": (49.7160419, 18.4481175),
        "MO HRANICE NA MORAVĚ": (49.5625267, 17.7384581),
        "MO MOHELNICE": (49.7783642, 16.9181650),
        "MO FRÝDEK-MÍSTEK": (49.6746753, 18.3348467),
        "MO ČRS PŘEROV": (49.4562222, 17.4612728),
        "MO TŘINEC": (49.6848167, 18.667728),
        "MO STARÁ VES NAD ODŘEJNICÍ": (49.7276794, 18.1881647),
        "MO ŠTERNBERK": (49.7249119, 17.2861164),
        "MO ČRS OSTRAVA": (49.8197344, 18.1727867),
        "MO ZLATÉ HORY": (50.2631267, 17.3953689),
        "MO ČESKÝ TĚŠÍN": (49.7437028, 18.6158606),
        "MO KARVINÁ": (49.9012592, 18.5424597),
        "MO VRBNO P. PRADĚDEM": (50.1218706, 17.3740400),
        "MO OLOMOUC": (49.6078183, 17.2831197),
        "MO STARÁ VES NAD ONDŘEJNICÍ": (49.7276794, 18.1881647),
        "MO HRANICE": (49.5625267, 17.7384581),
    }
