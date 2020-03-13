from production_code.common.constants import Constants


class NorthMoraviaAndSilesiaConstants:
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
        "https://www.rybsvaz-ms.cz/katalog/rybarske-reviry/mimopstruhove-reviry/filtrovani-polozek.php?recordStart=180",
    ]
    LOCATION_URL_PATTERN = ("<a href=\"(?P<"
                            + Constants.LOCATION_URL_PATTERN_GROUP_NAME
                            + ">/katalog/rybarske-reviry/mimopstruhove-reviry/.*.html)\"")

    HEADQUARTER_GPS = {
        "MO ŠTERNBERK": (49.7249119, 17.2861164),
        "MO VÍTKOV": (49.7749544, 17.7501242),
        "MO BARTOŠOVICE": (49.6688167, 18.0544589),
        "MO OSTRAVA": (49.8197344, 18.1727867),
        "MO FRÝDEK-MÍSTEK": (49.6746753, 18.3348467),
        "MO PŘEROV": (49.4562222, 17.4612942),
        "MO LIPNÍK NAD BEČVOU": (49.5249303, 17.5878428),
        "MO HRANICE NA MORAVĚ": (49.5625267, 17.7384581),
        "MO HUSTOPEČE NAD BEČVOU": (49.5302819, 17.8682694),
        "MO CHORYNĚ": (49.4965175, 17.8968361),
        "MO VALAŠSKÉ MEZIŘÍČÍ": (49.4575775, 17.9867503),
        "MO VSETÍN": (49.3337367, 17.9884181),
        "MO ŠUMPERK": (49.9668033, 16.9747031),
        "MO BÍLOVEC": (49.7599231, 18.0203639),
        "MO TOVAČOV": (49.4183917, 17.2889497),
        "MO OLOMOUC": (49.6078183, 17.2831197),
        "MO BRAVANTICE": (49.7672139, 18.0833636),
        "MO ZÁBŘEH NA MORAVĚ": (49.8780325, 16.8717022),
        "MO BRUNTÁL": (49.9733703, 17.4728339),
        "MO VELKÁ BYSTŘICE": (49.5931169, 17.3467811),
        "MO KRNOV": (50.0868806, 17.7093039),
        "MO HAVÍŘOV": (49.7710231, 18.5060006),
        "MO FULNEK": (49.7159878, 17.9070500),
        "MO TÍSEK": (49.7923706, 18.0170761),
        "MO JAVORNÍK": (50.3923175, 17.0079122),
        "MO NOVÝ JIČÍN": (49.5938208, 18.0121372),
        "MO KELČ": (49.4762997, 17.8182542),
        "MO KARVINÁ": (49.9012592, 18.5424597),
        "MO JISTEBNÍK": (49.7329161, 18.1505603),
        "MO PŘÍBOR": (49.6418581, 18.1490892),
        "MO FRENŠTÁT POD RADHOŠTĚM": (49.5496131, 18.2051661),
        "MO LUČINA": (49.7160419, 18.4481175),
        "MO BRODEK U PŘEROVA": (49.4841794, 17.3385214),
        "MO MILENOV": (49.5630281, 17.6680828),
        "MO KRAVAŘE": (49.9248225, 18.0021083),
        "MO LITOVEL": (49.6968167, 17.0743217),
        "MO MOHELNICE": (49.7783642, 16.9181650),
        "MO ZÁBŘEH": (49.8780258, 16.8718311),
        "MO OPAVA": (49.9366425, 17.9179214),
        "MO OLŠOVEC": (49.5930508, 17.7117214),
        "MO BOHUMÍN": (49.9017481, 18.3315467),
        "MO STUDÉNKA": (49.7147586, 18.0537189),
        "OÚ PUSTĚJOV (MO PUSTĚJOV)": (49.6963600, 18.0060328),
        "MO PASKOV": (49.7237736, 18.2976753),
        "MO ČESKÝ TĚŠÍN": (49.7437028, 18.6158606),
        "MO TŘINEC": (49.6848167, 18.6677281),
        "MO BYSTŘICE NAD OLŠÍ": (49.6367725, 18.7208733),
        "MO STARÁ VES N. O.": (49.7276794, 18.1881647),
        "MO STARÁ VES": (49.7276794, 18.1881647),
        "MO STARÁ VES N.O.": (49.7276794, 18.1881647),
        "MO HLUČÍN": (49.8970078, 18.1912983),
        "MO VRBNO POD PRADĚDEM": (50.1218706, 17.3740400),
        "MO ORLOVÁ": (49.8560450, 18.4135444),
        "MO UNIČOV": (49.7721319, 17.1204328),
        "MO RÝMAŘOV": (49.9316686, 17.2637747),
        "MO ZLATÉ HORY": (50.2631267, 17.3953689),
        "MO JESENÍK": (50.2177233, 17.2070200),
        "MO LOŠTICE": (49.7424722, 16.9219292),
    }
