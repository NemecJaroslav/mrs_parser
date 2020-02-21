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
        "471001",
        "471002",
        "471003",
        "471005",
        "471006",
        "471007",
        "471008",
        "471009",
        "471010",
        "471011",
        "471013",
        "471014",
        "471015",
        "471016",
        "471017",
        "471018",
        "471019",
        "471020",
        "471021",
        "471022",
    ]


def get_expected_location_names():
    return [
        "BALATON 1 A",
        "BAŠTICE 1 A",
        "BEČVA 1",
        "BEČVA 2",
        "BEČVA 2 A",
        "BEČVA 3",
        "BEČVA 3 A",
        "BEČVA 4",
        "BEČVA 4 A",
        "BEČVA 5",
        "BEČVA 6",
        "BEČVA 6 A",
        "BEČVA 7",
        "BEČVA 7 A",
        "BEČVA VSETÍNSKÁ 4 A",
        "BLATA 1",
        "BLATA 2",
        "BUDIŠOVKA 1 A",
        "BYSTŘICE HANÁCKÁ 1",
        "BYSTŘICE HANÁCKÁ 2 A",
    ]


def get_expected_headquarters():
    return [
        "MO VÍTKOV",
        "MO FRÝDEK-MÍSTEK",
        "MO PŘEROV",
        "MO PŘEROV",
        "MO PŘEROV",
        "MO LIPNÍK NAD BEČVOU",
        "MO LIPNÍK NAD BEČVOU",
        "MO HRANICE NA MORAVĚ",  # 32 vs 160 ascii after "NA"
        "MO HRANICE NA MORAVĚ",  # 32 vs 160 ascii after "NA"
        "MO HUSTOPEČE NAD BEČVOU",
        "MO CHORYNĚ",
        "MO CHORYNĚ",
        "MO VALAŠSKÉ MEZIŘÍČÍ",
        "MO VALAŠSKÉ MEZIŘÍČÍ",
        "MO VSETÍN",
        "MO TOVAČOV",
        "MO OLOMOUC",
        "MO VÍTKOV",
        "MO OLOMOUC",
        "MO VELKÁ BYSTŘICE",
    ]


def get_expected_area():
    return [
        5.5,
        32.0,
        36.0,
        35.0,
        12.3,
        23.0,
        4.35,
        35.0,
        26.0,
        16.0,
        13.0,
        2.5,
        17.0,
        9.45,
        5.0,
        11.0,
        5.0,
        12.0,
        5.0,
        2.2,
    ]


def get_expected_gps():
    return [
        [],
        [(GPSCoordinate(49, 38, 54.44, "N"), GPSCoordinate(18, 22, 30.034, "E"))],
        [(GPSCoordinate(49, 25, 54.222, "N"), GPSCoordinate(17, 20, 1.972, "E")),
         (GPSCoordinate(49, 26, 57.105, "N"), GPSCoordinate(17, 26, 17.462, "E"))],
        [(GPSCoordinate(49, 26, 57.196, "N"), GPSCoordinate(17, 26, 17.74, "E")),
         (GPSCoordinate(49, 30, 36.355, "N"), GPSCoordinate(17, 33, 46.164, "E")),
         (GPSCoordinate(49, 26, 59.29, "N"), GPSCoordinate(17, 25, 34.428, "E")),
         (GPSCoordinate(49, 30, 4.197, "N"), GPSCoordinate(17, 30, 28.906, "E"))],
        [(GPSCoordinate(49, 29, 29.499, "N"), GPSCoordinate(17, 31, 25.276, "E")),
         (GPSCoordinate(49, 29, 49.703, "N"), GPSCoordinate(17, 30, 14.764, "E")),
         (GPSCoordinate(49, 29, 48.73, "N"), GPSCoordinate(17, 30, 26.051, "E")),
         (GPSCoordinate(49, 27, 41.285, "N"), GPSCoordinate(17, 28, 4.445, "E")),
         (GPSCoordinate(49, 27, 36.045, "N"), GPSCoordinate(17, 27, 47.027, "E"))],
        [(GPSCoordinate(49, 30, 36.368, "N"), GPSCoordinate(17, 33, 46.314, "E")),
         (GPSCoordinate(49, 31, 42.086, "N"), GPSCoordinate(17, 39, 3.508, "E")),
         (GPSCoordinate(49, 30, 4.245, "N"), GPSCoordinate(17, 30, 28.933, "E")),
         (GPSCoordinate(49, 30, 37.866, "N"), GPSCoordinate(17, 33, 46.641, "E"))],
        [(GPSCoordinate(49, 33, 48.69, "N"), GPSCoordinate(17, 35, 3.24, "E")),
         (GPSCoordinate(49, 31, 19.716, "N"), GPSCoordinate(17, 35, 47.543, "E")),
         (GPSCoordinate(49, 31, 49.945, "N"), GPSCoordinate(17, 37, 53.415, "E")),
         (GPSCoordinate(49, 31, 6.515, "N"), GPSCoordinate(17, 34, 45.482, "E")),
         (GPSCoordinate(49, 31, 33.498, "N"), GPSCoordinate(17, 38, 43.217, "E"))],
        [(GPSCoordinate(49, 31, 42.068, "N"), GPSCoordinate(17, 39, 3.557, "E")),
         (GPSCoordinate(49, 31, 46.604, "N"), GPSCoordinate(17, 47, 19.809, "E"))],
        [(GPSCoordinate(49, 32, 32.095, "N"), GPSCoordinate(17, 42, 38.124, "E")),
         (GPSCoordinate(49, 32, 32.65, "N"), GPSCoordinate(17, 43, 16.888, "E")),
         (GPSCoordinate(49, 32, 47.401, "N"), GPSCoordinate(17, 46, 58.385, "E"))],
        [(GPSCoordinate(49, 31, 46.651, "N"), GPSCoordinate(17, 47, 19.862, "E")),
         (GPSCoordinate(49, 30, 37.001, "N"), GPSCoordinate(17, 52, 38.427, "E")),
         (GPSCoordinate(49, 31, 48.682, "N"), GPSCoordinate(17, 48, 23.83, "E"))],
        [(GPSCoordinate(49, 30, 36.935, "N"), GPSCoordinate(17, 52, 38.473, "E")),
         (GPSCoordinate(49, 29, 44.787, "N"), GPSCoordinate(17, 56, 28.321, "E"))],
        [(GPSCoordinate(49, 30, 27.656, "N"), GPSCoordinate(17, 53, 45.905, "E"))],
        [(GPSCoordinate(49, 29, 44.668, "N"), GPSCoordinate(17, 56, 28.513, "E")),
         (GPSCoordinate(49, 28, 12.447, "N"), GPSCoordinate(17, 57, 15.989, "E"))],
        [(GPSCoordinate(49, 27, 22.448, "N"), GPSCoordinate(17, 58, 25.098, "E")),
         (GPSCoordinate(49, 27, 25.489, "N"), GPSCoordinate(17, 58, 18.935, "E")),
         (GPSCoordinate(49, 27, 18.459, "N"), GPSCoordinate(17, 53, 26.298, "E")),
         (GPSCoordinate(49, 29, 30.646, "N"), GPSCoordinate(17, 56, 35.143, "E"))],
        [(GPSCoordinate(49, 20, 42.571, "N"), GPSCoordinate(18, 12, 57.081, "E"))],
        [(GPSCoordinate(49, 25, 3.851, "N"), GPSCoordinate(17, 17, 9.163, "E")),
         (GPSCoordinate(49, 30, 50.253, "N"), GPSCoordinate(17, 12, 42.389, "E")),
         (GPSCoordinate(49, 23, 48.777, "N"), GPSCoordinate(17, 18, 23.506, "E")),
         (GPSCoordinate(49, 24, 13.071, "N"), GPSCoordinate(17, 17, 31.965, "E")),
         (GPSCoordinate(49, 25, 3.952, "N"), GPSCoordinate(17, 17, 9.163, "E")),
         (GPSCoordinate(49, 30, 50.253, "N"), GPSCoordinate(17, 12, 42.389, "E"))],
        [(GPSCoordinate(49, 30, 50.321, "N"), GPSCoordinate(17, 12, 42.218, "E")),
         (GPSCoordinate(49, 37, 21.897, "N"), GPSCoordinate(17, 2, 3.528, "E"))],
        [(GPSCoordinate(49, 48, 5.021, "N"), GPSCoordinate(17, 35, 19.724, "E")),
         (GPSCoordinate(49, 47, 23.766, "N"), GPSCoordinate(17, 37, 58.673, "E")),
         (GPSCoordinate(49, 47, 46.03, "N"), GPSCoordinate(17, 37, 6.562, "E")),
         (GPSCoordinate(49, 45, 22.541, "N"), GPSCoordinate(17, 30, 21.046, "E")),
         (GPSCoordinate(49, 50, 11.879, "N"), GPSCoordinate(17, 33, 42.977, "E"))],
        [(GPSCoordinate(49, 35, 33.984, "N"), GPSCoordinate(17, 16, 6.099, "E")),
         (GPSCoordinate(49, 35, 38.107, "N"), GPSCoordinate(17, 19, 52.823, "E")),
         (GPSCoordinate(49, 33, 37.021, "N"), GPSCoordinate(17, 16, 7.174, "E")),
         (GPSCoordinate(49, 35, 35.823, "N"), GPSCoordinate(17, 19, 9.371, "E"))],
        [(GPSCoordinate(49, 37, 24.67, "N"), GPSCoordinate(17, 21, 56.106, "E")),
         (GPSCoordinate(49, 33, 52.876, "N"), GPSCoordinate(17, 23, 5.242, "E")),
         (GPSCoordinate(49, 36, 23.268, "N"), GPSCoordinate(17, 20, 55.276, "E"))],
    ]
