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
    ]
