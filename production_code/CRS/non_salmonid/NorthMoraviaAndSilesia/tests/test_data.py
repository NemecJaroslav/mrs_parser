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
    ]


def get_expected_location_names():
    return [
        "BALATON 1 A",
        "BAŠTICE 1 A",
        "BEČVA 1",
    ]


def get_expected_headquarters():
    return [
        "MO VÍTKOV",
        "MO FRÝDEK-MÍSTEK",
        "MO PŘEROV",
    ]


def get_expected_area():
    return [
        5.5,
        32.0,
        36.0,
    ]


def get_expected_gps():
    return [
        [],
        [(GPSCoordinate(49, 38, 54.44, "N"), GPSCoordinate(18, 22, 30.034, "E"))],
        [(GPSCoordinate(49, 25, 54.222, "N"), GPSCoordinate(17, 20, 1.972, "E")),
         (GPSCoordinate(49, 26, 57.105, "N"), GPSCoordinate(17, 26, 17.462, "E"))],
    ]
