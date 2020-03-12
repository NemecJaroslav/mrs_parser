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
    ]


def get_expected_location_names():
    return [
        "BEČVA ROŽNOVSKÁ 1",
    ]


def get_expected_headquarters():
    return [
        "MO VALAŠSKÉ MEZIŘÍČÍ",
    ]


def get_expected_area():
    return [
        8.0,
    ]


def get_expected_gps():
    return [
        [(GPSCoordinate(49, 28, 23.571, "N"), GPSCoordinate(17, 58, 24.85, "E")),
         (GPSCoordinate(49, 27, 50.285, "N"), GPSCoordinate(18, 3, 14.505, "E"))],
    ]
