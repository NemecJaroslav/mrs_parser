from production_code.common.fishing_location import FishingLocation
from production_code.common.parser import GPSCoordinate


def get_expected_fishing_locations():
    expected_fishing_locations = []

    for (location_id,
         location_name,
         headquarter,
         area,
         gps) in zip(get_expected_location_ids(),
                     get_expected_location_names(),
                     get_expected_headquarters(),
                     get_expected_area(),
                     get_expected_gps()):
        expected_fishing_locations.append(
            FishingLocation(
                location_id,
                location_name,
                headquarter,
                area,
                gps,
            )
        )

    return expected_fishing_locations


def get_expected_location_ids():
    return [
        "473001",
        "473002",
        "473003",
        "473004",
        "473005",
        "473006",
        "473007",
        "473008",
        "473009",
        "473010",
        "473011",
        "473012",
        "473013",
        "473014",
        "473015",
        "473016",
        "473017",
        "473018",
        "473019",
        "473021",
        "473022",
        "473023",
        "473024",
        "473025",
        "473026",
        "473027",
        "473028",
        "473029",
        "473030",
        "473031",
        "473032",
        "473033",
        "473034",
        "473035",
        "473036",
        "473037",
        "473038",
        "473039",
        "473040",
        "473041",
        "473042",
        "473043",
        "473044",
        "473045",
        "473046",
        "473047",
        "473048",
        "473049",
        "473050",
        "473051",
        "473052",
        "473053",
        "473054",
        "473056",
        "473057",
        "473058",
        "473059",
        "473061",
        "473062",
        "473063",
        "473064",
        "473065",
        "473066",
        "473067",
        "473068",
        "473069",
        "473070",
        "473071",
        "473072",
        "473073",
        "473074",
    ]


def get_expected_location_names():
    return [
        "BEČVA ROŽNOVSKÁ 1",
        "BEČVA ROŽNOVSKÁ 2",
        "BEČVA VSETÍNSKÁ 1",
        "BEČVA VSETÍNSKÁ 2",
        "BEČVA VSETÍNSKÁ 3",
        "BEČVA VSETÍNSKÁ 4 P",
        "BĚLÁ JESENICKÁ 1",
        "BĚLÁ JESENICKÁ 2",
        "BÍLOVKA 1",
        "BRANNÁ 1",
        "BŘEZNÁ 1",
        "BŘEZNÁ 2",
        "BUDIŠOVKA 1 P",
        "BYSTŘICE HANÁCKÁ 2 P",
        "BYSTŘICE HANÁCKÁ 3",
        "BYSTŘICE HANÁCKÁ 4",
        "BYSTŘICE VALAŠSKÁ 1 P",
        "ČELADENKA 1",
        "ČERNÁ OPAVA 1",
        "ČERVENÝ POTOK 1",
        "HOŘINA 1",
        "DESNÁ 2",
        "DESNÁ 3",
        "HERLIČKA 1",
        "HLUCHOVÁ 1",
        "HROZOVÁ 1",
        "HVOZDNICE 1",
        "HUSÍ POTOK 1",
        "JAVORNICKÝ POTOK",
        "JIČÍNKA 2",
        "JUHYNĚ 1",
        "JUHYNĚ 2",
        "KLENOS 1",
        "KOČOVSKÝ POTOK 1",
        "KRUPÁ 1",
        "LAZNICKÝ POTOK 1",
        "LIBINA 1 P",
        "LOMNÁ 1",
        "LOSINKA 1",
        "LUBINA 2 P",
        "LUBINA 3",
        "LUČINA 1 P",
        "LUČINA 3",
        "LUDINA 1",
        "LUHA 1",
        "LUHA 2",
        "MERTA 1",
        "MOHELNICE 1",
        "MORAVA 23",
        "MORAVICE 1 P",
        "MORAVICE 2",
        "MORAVICE 3 P",
        "MORAVICE 4",
        "MORAVICE 7",
        "MORAVICE 8",
        "MORÁVKA 1",
        "ODRA 8",
        "OLEŠNÁ 3",
        "OLEŠNICE JESENICKÁ 1",
        "OLEŠNICE PŘEROVSKÁ 2",
        "OLŠE 5 P",
        "OLŠE 6",
        "OLŠE 7",
        "ONDŘEJNICE 2",
        "OPAVA 7",
        "OPAVA 8",
        "OPAVICE (ZLATÁ) 1",
        "OPAVICE (ZLATÁ) 2",
        "OSKAVA 4",
        "OSLAVA ŠTERNBERSKÁ 1",
        "OSOBLAHA 2",
    ]


def get_expected_headquarters():
    return [
        "MO VALAŠSKÉ MEZIŘÍČÍ",
        "MO ROŽNOV POD RADHOŠTĚM",
        "MO VALAŠSKÉ MEZIŘÍČÍ",
        "MO VSETÍN",
        "MO VSETÍN",
        "MO VSETÍN",
        "MO JESENÍK",
        "MO JESENÍK",
        "MO BÍLOVEC",
        "MO ŠUMPERK",
        "MO ZÁBŘEH NA MORAVĚ",  # 32 vs 160 ascii after "NA"
        "MO ZÁBŘEH NA MORAVĚ",  # 32 vs 160 ascii after "NA"
        "MO VÍTKOV",
        "MO VELKÁ BYSTŘICE",
        "MO DOMAŠOV NAD BYSTŘICÍ",
        "MO DOMAŠOV NAD BYSTŘICÍ",
        "MO VSETÍN",
        "MO FRÝDLANT NAD OSTRAVICÍ",
        "MO VRBNO POD PRADĚDEM",
        "MO JAVORNÍK",
        "MO KRNOV",
        "MO ŠUMPERK",
        "MO ŠUMPERK",
        "MO OPAVA",
        "MO BYSTŘICE NAD OLŠÍ",
        "MO KRNOV",
        "MO OPAVA",
        "MO FULNEK",
        "MO JAVORNÍK",
        "MO NOVÝ JIČÍN",
        "MO CHORYNĚ",
        "MO KELČ",
        "MO PŘÍBOR",
        "MO RÝMAŘOV",
        "MO ŠUMPERK",
        "MO LIPNÍK NAD BEČVOU",
        "MO UNIČOV",
        "MO JABLUNKOV",
        "MO ŠUMPERK",
        "MO PŘÍBOR",
        "MO FRENŠTÁT POD RADHOŠTĚM",
        "MO HAVÍŘOV",
        "MO LUČINA",
        "MO HRANICE NA MORAVĚ",  # 32 vs 160 ascii after "NA"
        "MO NOVÝ JIČÍN",
        "MO HRANICE NA MORAVĚ",  # 32 vs 160 ascii after "NA"
        "MO ŠUMPERK",
        "MO FRÝDEK-MÍSTEK",
        "MO ŠUMPERK",
        "MO OPAVA",
        "MO OPAVA",
        "MO VÍTKOV",
        "MO VÍTKOV",
        "MO RÝMAŘOV",
        "MO RÝMAŘOV",
        "MO FRÝDEK-MÍSTEK",
        "MO VÍTKOV",
        "MO FRÝDEK-MÍSTEK",
        "MO JESENÍK",
        "MO LIPNÍK NAD BEČVOU",
        "MO TŘINEC",
        "MO BYSTŘICE NAD OLŠÍ",
        "MO JABLUNKOV",
        "MO STARÁ VES NAD ODŘEJNICÍ",
        "MO KRNOV",
        "MO BRUNTÁL",
        "MO KRNOV",
        "MO KRNOV",
        "MO UNIČOV",
        "MO ŠTERNBERK",
        "MO KRNOV",
    ]


def get_expected_area():
    return [
        8.0,
        27.4,
        16.0,
        22.0,
        11.0,
        14.0,
        19.0,
        11.0,
        7.0,
        10.0,
        8.0,
        6.0,
        4.0,
        4.0,
        7.0,
        7.5,
        4.0,
        7.0,
        16.0,
        3.0,
        2.0,
        11.0,
        11.0,
        3.0,
        4.0,
        3.0,
        14.0,
        6.0,
        3.5,
        8.0,
        2.0,
        8.0,
        2.0,
        2.5,
        6.0,
        2.0,
        2.4,
        4.0,
        5.0,
        6.6,
        12.8,
        8.0,
        13.0,
        4.0,
        6.0,
        2.0,
        6.0,
        6.0,
        30.0,
        13.0,
        18.0,
        18.0,
        13.0,
        12.0,
        10.0,
        43.0,
        19.0,
        3.0,
        5.0,
        5.0,
        6.0,
        6.5,
        12.0,
        15.0,
        17.0,
        15.0,
        8.0,
        8.0,
        8.0,
        7.5,
        9.0,
    ]


def get_expected_gps():
    return [
        [(GPSCoordinate(49, 28, 23.571, "N"), GPSCoordinate(17, 58, 24.85, "E")),
         (GPSCoordinate(49, 27, 50.285, "N"), GPSCoordinate(18, 3, 14.505, "E"))],
        [(GPSCoordinate(49, 27, 50.284, "N"), GPSCoordinate(18, 3, 14.53, "E")),
         (GPSCoordinate(49, 25, 21.042, "N"), GPSCoordinate(18, 18, 50.902, "E")),
         (GPSCoordinate(49, 25, 24.142, "N"), GPSCoordinate(18, 19, 5.337, "E"))],
        [(GPSCoordinate(49, 28, 12.059, "N"), GPSCoordinate(17, 57, 15.966, "E")),
         (GPSCoordinate(49, 25, 9.233, "N"), GPSCoordinate(17, 57, 35.957, "E"))],
        [(GPSCoordinate(49, 25, 9.391, "N"), GPSCoordinate(17, 57, 34.849, "E")),
         (GPSCoordinate(49, 19, 29.199, "N"), GPSCoordinate(17, 59, 48.483, "E"))],
        [(GPSCoordinate(49, 19, 28.692, "N"), GPSCoordinate(17, 59, 48.081, "E")),
         (GPSCoordinate(49, 19, 32.139, "N"), GPSCoordinate(18, 9, 46.821, "E"))],
        [(GPSCoordinate(49, 19, 32.134, "N"), GPSCoordinate(18, 9, 47.019, "E")),
         (GPSCoordinate(49, 23, 51.182, "N"), GPSCoordinate(18, 23, 51.103, "E"))],
        [(GPSCoordinate(50, 18, 23.981, "N"), GPSCoordinate(17, 21, 11.436, "E")),
         (GPSCoordinate(50, 15, 15.521, "N"), GPSCoordinate(17, 13, 32.006, "E"))],
        [(GPSCoordinate(50, 14, 9.889, "N"), GPSCoordinate(17, 12, 13.597, "E")),
         (GPSCoordinate(50, 7, 8.223, "N"), GPSCoordinate(17, 14, 8.987, "E"))],
        [(GPSCoordinate(49, 43, 34.6, "N"), GPSCoordinate(18, 8, 2.034, "E")),
         (GPSCoordinate(49, 46, 36.531, "N"), GPSCoordinate(17, 58, 0.666, "E"))],
        [(GPSCoordinate(50, 4, 35.656, "N"), GPSCoordinate(16, 56, 4.023, "E")),
         (GPSCoordinate(50, 8, 53.277, "N"), GPSCoordinate(17, 0, 48.952, "E"))],
        [(GPSCoordinate(49, 52, 26.988, "N"), GPSCoordinate(16, 46, 9.840, "E")),
         (GPSCoordinate(49, 57, 18.261, "N"), GPSCoordinate(16, 46, 1.338, "E"))],
        [(GPSCoordinate(49, 57, 18.634, "N"), GPSCoordinate(16, 46, 1.326, "E")),
         (GPSCoordinate(50, 1, 10.706, "N"), GPSCoordinate(16, 44, 43.571, "E"))],
        [(GPSCoordinate(49, 44, 6.731, "N"), GPSCoordinate(17, 41, 37.588, "E")),
         (GPSCoordinate(49, 48, 3.918, "N"), GPSCoordinate(17, 35, 34.638, "E"))],
        [(GPSCoordinate(49, 35, 38.146, "N"), GPSCoordinate(17, 19, 52.912, "E")),
         (GPSCoordinate(49, 39, 15.305, "N"), GPSCoordinate(17, 24, 38.151, "E"))],
        [(GPSCoordinate(49, 39, 15.305, "N"), GPSCoordinate(17, 24, 38.151, "E")),
         (GPSCoordinate(49, 44, 33.129, "N"), GPSCoordinate(17, 26, 46.811, "E")),
         (GPSCoordinate(49, 44, 54.742, "N"), GPSCoordinate(17, 27, 21.01, "E"))],
        [(GPSCoordinate(49, 44, 33.162, "N"), GPSCoordinate(17, 26, 46.763, "E")),
         (GPSCoordinate(49, 50, 2.747, "N"), GPSCoordinate(17, 24, 2.368, "E")),
         (GPSCoordinate(49, 46, 50.737, "N"), GPSCoordinate(17, 26, 29.686, "E")),
         (GPSCoordinate(49, 47, 51.145, "N"), GPSCoordinate(17, 26, 44.507, "E"))],
        [(GPSCoordinate(49, 25, 12.295, "N"), GPSCoordinate(17, 57, 51.085, "E")),
         (GPSCoordinate(49, 23, 41.621, "N"), GPSCoordinate(18, 9, 45.035, "E"))],
        [(GPSCoordinate(49, 34, 7.52, "N"), GPSCoordinate(18, 21, 45.99, "E")),
         (GPSCoordinate(49, 27, 11.437, "N"), GPSCoordinate(18, 22, 13.214, "E")),
         (GPSCoordinate(49, 34, 3.787, "N"), GPSCoordinate(18, 21, 17.844, "E")),
         (GPSCoordinate(49, 34, 4.612, "N"), GPSCoordinate(18, 21, 31.82, "E"))],
        [(GPSCoordinate(50, 7, 32.177, "N"), GPSCoordinate(17, 22, 47.336, "E")),
         (GPSCoordinate(50, 10, 49.228, "N"), GPSCoordinate(17, 17, 12.07, "E"))],
        [(GPSCoordinate(50, 21, 46.532, "N"), GPSCoordinate(17, 9, 53.885, "E")),
         (GPSCoordinate(50, 17, 46.251, "N"), GPSCoordinate(17, 10, 32.787, "E")),
         (GPSCoordinate(50, 20, 41.15, "N"), GPSCoordinate(17, 10, 34.049, "E")),
         (GPSCoordinate(50, 19, 4.662, "N"), GPSCoordinate(17, 10, 1.573, "E"))],
        [(GPSCoordinate(50, 1, 10.166, "N"), GPSCoordinate(17, 46, 23.63, "E")),
         (GPSCoordinate(49, 58, 51.197, "N"), GPSCoordinate(17, 39, 0.735, "E"))],
        [(GPSCoordinate(49, 57, 11.642, "N"), GPSCoordinate(16, 59, 25.638, "E")),
         (GPSCoordinate(50, 4, 9.264, "N"), GPSCoordinate(17, 5, 13.452, "E"))],
        [(GPSCoordinate(50, 4, 9.265, "N"), GPSCoordinate(17, 5, 13.427, "E")),
         (GPSCoordinate(50, 5, 56.594, "N"), GPSCoordinate(17, 6, 26.027, "E")),
         (GPSCoordinate(50, 5, 56.626, "N"), GPSCoordinate(17, 6, 26.054, "E")),
         (GPSCoordinate(50, 9, 5.852, "N"), GPSCoordinate(17, 7, 21.012, "E")),
         (GPSCoordinate(50, 5, 56.594, "N"), GPSCoordinate(17, 6, 26.027, "E")),
         (GPSCoordinate(50, 5, 17.404, "N"), GPSCoordinate(17, 10, 49.374, "E"))],
        [(GPSCoordinate(49, 59, 33.806, "N"), GPSCoordinate(17, 49, 17.372, "E")),
         (GPSCoordinate(49, 58, 6.23, "N"), GPSCoordinate(17, 43, 54.446, "E"))],
        [(GPSCoordinate(49, 37, 53.166, "N"), GPSCoordinate(18, 43, 0.341, "E")),
         (GPSCoordinate(49, 39, 20.937, "N"), GPSCoordinate(18, 45, 31.453, "E"))],
        [(GPSCoordinate(50, 14, 41.992, "N"), GPSCoordinate(17, 43, 5.318, "E")),
         (GPSCoordinate(50, 10, 45.482, "N"), GPSCoordinate(17, 36, 26.9, "E"))],
        [(GPSCoordinate(49, 54, 15.574, "N"), GPSCoordinate(17, 53, 53.376, "E")),
         (GPSCoordinate(49, 55, 0.676, "N"), GPSCoordinate(17, 41, 29.259, "E")),
         (GPSCoordinate(49, 56, 46.803, "N"), GPSCoordinate(17, 39, 30.639, "E"))],
        [(GPSCoordinate(49, 40, 40.018, "N"), GPSCoordinate(18, 0, 35.324, "E")),
         (GPSCoordinate(49, 45, 20.627, "N"), GPSCoordinate(17, 49, 16.184, "E"))],
        [(GPSCoordinate(50, 24, 41.39, "N"), GPSCoordinate(17, 2, 32.567, "E")),
         (GPSCoordinate(50, 22, 21.666, "N"), GPSCoordinate(16, 55, 55.825, "E"))],
        [(GPSCoordinate(49, 37, 34.888, "N"), GPSCoordinate(17, 59, 29.21, "E")),
         (GPSCoordinate(49, 31, 11.382, "N"), GPSCoordinate(18, 8, 27.675, "E")),
         (GPSCoordinate(49, 35, 20.764, "N"), GPSCoordinate(18, 1, 20.94, "E")),
         (GPSCoordinate(49, 31, 37.149, "N"), GPSCoordinate(18, 1, 10.668, "E")),
         (GPSCoordinate(49, 33, 27.951, "N"), GPSCoordinate(18, 1, 22.359, "E")),
         (GPSCoordinate(49, 32, 43.52, "N"), GPSCoordinate(17, 58, 19.751, "E"))],
        [(GPSCoordinate(49, 30, 12.252, "N"), GPSCoordinate(17, 53, 42.173, "E")),
         (GPSCoordinate(49, 29, 30.503, "N"), GPSCoordinate(17, 53, 23.45, "E"))],
        [(GPSCoordinate(49, 29, 30.503, "N"), GPSCoordinate(17, 53, 23.45, "E")),
         (GPSCoordinate(49, 25, 42.254, "N"), GPSCoordinate(17, 47, 14.74, "E"))],
        [],
        [(GPSCoordinate(49, 55, 29.62, "N"), GPSCoordinate(17, 27, 7.82, "E")),
         (GPSCoordinate(49, 58, 47.708, "N"), GPSCoordinate(17, 22, 27.173, "E"))],
        [(GPSCoordinate(50, 5, 18.23, "N"), GPSCoordinate(16, 55, 11.809, "E")),
         (GPSCoordinate(50, 10, 4.259, "N"), GPSCoordinate(16, 56, 36.087, "E"))],
        [],
        [(GPSCoordinate(49, 52, 53.96, "N"), GPSCoordinate(17, 5, 7.215, "E"))],
        [(GPSCoordinate(49, 34, 45.391, "N"), GPSCoordinate(18, 45, 50.995, "E")),
         (GPSCoordinate(49, 31, 19.39, "N"), GPSCoordinate(18, 37, 55.943, "E"))],
        [],
        [(GPSCoordinate(49, 39, 31.9, "N"), GPSCoordinate(18, 8, 31.252, "E")),
         (GPSCoordinate(49, 37, 2.425, "N"), GPSCoordinate(18, 10, 10.452, "E"))],
        [(GPSCoordinate(49, 37, 2.407, "N"), GPSCoordinate(18, 10, 10.526, "E")),
         (GPSCoordinate(49, 30, 35.798, "N"), GPSCoordinate(18, 11, 53.956, "E")),
         (GPSCoordinate(49, 35, 24.898, "N"), GPSCoordinate(18, 11, 37.716, "E")),
         (GPSCoordinate(49, 32, 18.12, "N"), GPSCoordinate(18, 16, 59.359, "E")),
         (GPSCoordinate(49, 33, 14.135, "N"), GPSCoordinate(18, 12, 5.547, "E")),
         (GPSCoordinate(49, 30, 27.738, "N"), GPSCoordinate(18, 14, 49.754, "E")),
         (GPSCoordinate(49, 34, 41.261, "N"), GPSCoordinate(18, 10, 57.191, "E")),
         (GPSCoordinate(49, 33, 0.041, "N"), GPSCoordinate(18, 9, 36.622, "E")),
         (GPSCoordinate(49, 32, 27.301, "N"), GPSCoordinate(18, 13, 48.549, "E")),
         (GPSCoordinate(49, 31, 29.155, "N"), GPSCoordinate(18, 15, 52.761, "E"))],
        [(GPSCoordinate(49, 46, 8.553, "N"), GPSCoordinate(18, 26, 0.987, "E")),
         (GPSCoordinate(49, 43, 56.545, "N"), GPSCoordinate(18, 26, 45.254, "E"))],
        [(GPSCoordinate(49, 41, 40.698, "N"), GPSCoordinate(18, 27, 44.515, "E")),
         (GPSCoordinate(49, 39, 2.301, "N"), GPSCoordinate(18, 27, 6.398, "E"))],
        [(GPSCoordinate(49, 32, 46.289, "N"), GPSCoordinate(17, 43, 48.307, "E")),
         (GPSCoordinate(49, 37, 58.181, "N"), GPSCoordinate(17, 43, 57.59, "E"))],
        [(GPSCoordinate(49, 37, 1.241, "N"), GPSCoordinate(17, 55, 29.074, "E")),
         (GPSCoordinate(49, 34, 21.102, "N"), GPSCoordinate(17, 52, 26.231, "E"))],
        [(GPSCoordinate(49, 34, 20.771, "N"), GPSCoordinate(17, 52, 25.241, "E")),
         (GPSCoordinate(49, 39, 58.581, "N"), GPSCoordinate(17, 44, 28.936, "E"))],
        [(GPSCoordinate(50, 0, 12.195, "N"), GPSCoordinate(17, 1, 29.653, "E")),
         (GPSCoordinate(50, 1, 53.042, "N"), GPSCoordinate(17, 7, 40.921, "E"))],
        [],
        [(GPSCoordinate(49, 56, 32.25, "N"), GPSCoordinate(16, 54, 0.346, "E")),
         (GPSCoordinate(50, 5, 17.752, "N"), GPSCoordinate(16, 55, 12.293, "E"))],
        [(GPSCoordinate(49, 54, 22.56, "N"), GPSCoordinate(17, 54, 29.299, "E")),
         (GPSCoordinate(49, 51, 36.973, "N"), GPSCoordinate(17, 51, 41.339, "E"))],
        [(GPSCoordinate(49, 51, 37.008, "N"), GPSCoordinate(17, 51, 41.241, "E")),
         (GPSCoordinate(49, 48, 33.335, "N"), GPSCoordinate(17, 47, 57.084, "E")),
         (GPSCoordinate(49, 51, 4.548, "N"), GPSCoordinate(17, 50, 30.576, "E")),
         (GPSCoordinate(49, 49, 52.754, "N"), GPSCoordinate(17, 49, 53.321, "E"))],
        [(GPSCoordinate(49, 48, 33.302, "N"), GPSCoordinate(17, 47, 57.082, "E")),
         (GPSCoordinate(49, 49, 14.211, "N"), GPSCoordinate(17, 42, 58.307, "E"))],
        [(GPSCoordinate(49, 49, 14.16, "N"), GPSCoordinate(17, 42, 57.053, "E")),
         (GPSCoordinate(49, 49, 26.637, "N"), GPSCoordinate(17, 40, 6.7, "E"))],
        [(GPSCoordinate(49, 55, 29.627, "N"), GPSCoordinate(17, 27, 8.222, "E")),
         (GPSCoordinate(49, 56, 6.386, "N"), GPSCoordinate(17, 20, 44.715, "E"))],
        [(GPSCoordinate(49, 56, 6.534, "N"), GPSCoordinate(17, 20, 44.597, "E")),
         (GPSCoordinate(50, 2, 20.397, "N"), GPSCoordinate(17, 15, 48.056, "E")),
         (GPSCoordinate(50, 1, 29.757, "N"), GPSCoordinate(17, 15, 26.122, "E")),
         (GPSCoordinate(50, 1, 53.162, "N"), GPSCoordinate(17, 14, 49.013, "E")),
         (GPSCoordinate(50, 1, 36.472, "N"), GPSCoordinate(17, 16, 29.346, "E")),
         (GPSCoordinate(50, 1, 17.104, "N"), GPSCoordinate(17, 14, 48.963, "E"))],
        [],
        [(GPSCoordinate(49, 41, 2.263, "N"), GPSCoordinate(17, 48, 4.186, "E")),
         (GPSCoordinate(49, 44, 6.663, "N"), GPSCoordinate(17, 41, 37.734, "E"))],
        [],
        [],
        [(GPSCoordinate(49, 30, 59.912, "N"), GPSCoordinate(17, 25, 21.586, "E")),
         (GPSCoordinate(49, 32, 39.398, "N"), GPSCoordinate(17, 25, 34.072, "E"))],
        [(GPSCoordinate(49, 41, 4.303, "N"), GPSCoordinate(18, 39, 7.158, "E")),
         (GPSCoordinate(49, 38, 28.076, "N"), GPSCoordinate(18, 42, 3.546, "E"))],
        [(GPSCoordinate(49, 38, 27.57, "N"), GPSCoordinate(18, 42, 3.657, "E")),
         (GPSCoordinate(49, 36, 11.368, "N"), GPSCoordinate(18, 44, 14.901, "E"))],
        [(GPSCoordinate(49, 36, 11.369, "N"), GPSCoordinate(18, 44, 14.877, "E")),
         (GPSCoordinate(49, 33, 40.979, "N"), GPSCoordinate(18, 50, 41.738, "E")),
         (GPSCoordinate(49, 34, 53.491, "N"), GPSCoordinate(18, 44, 43.617, "E"))],
        [(GPSCoordinate(49, 43, 16.261, "N"), GPSCoordinate(18, 11, 41.435, "E")),
         (GPSCoordinate(49, 40, 16.969, "N"), GPSCoordinate(18, 13, 34.24, "E"))],
        [(GPSCoordinate(50, 5, 0.441, "N"), GPSCoordinate(17, 44, 10.561, "E")),
         (GPSCoordinate(50, 1, 5.247, "N"), GPSCoordinate(17, 32, 34.073, "E"))],
        [(GPSCoordinate(50, 1, 5.264, "N"), GPSCoordinate(17, 32, 34.048, "E")),
         (GPSCoordinate(50, 3, 49.286, "N"), GPSCoordinate(17, 28, 33.902, "E"))],
        [(GPSCoordinate(50, 5, 45.907, "N"), GPSCoordinate(17, 42, 58.292, "E")),
         (GPSCoordinate(50, 9, 45.497, "N"), GPSCoordinate(17, 34, 51.028, "E"))],
        [(GPSCoordinate(50, 9, 45.805, "N"), GPSCoordinate(17, 34, 50.263, "E")),
         (GPSCoordinate(50, 9, 45.905, "N"), GPSCoordinate(17, 28, 12.699, "E"))],
        [(GPSCoordinate(49, 49, 6.518, "N"), GPSCoordinate(17, 6, 35.729, "E")),
         (GPSCoordinate(49, 55, 51.027, "N"), GPSCoordinate(17, 9, 15.252, "E")),
         (GPSCoordinate(49, 53, 26.968, "N"), GPSCoordinate(17, 7, 42.545, "E"))],
        [(GPSCoordinate(49, 47, 44.678, "N"), GPSCoordinate(17, 7, 41.633, "E")),
         (GPSCoordinate(49, 54, 40.897, "N"), GPSCoordinate(17, 17, 52.372, "E"))],
        [(GPSCoordinate(50, 14, 7.591, "N"), GPSCoordinate(17, 41, 3.221, "E")),
         (GPSCoordinate(50, 12, 41.554, "N"), GPSCoordinate(17, 25, 25.808, "E"))],
    ]
