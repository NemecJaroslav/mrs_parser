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
    ]


def get_expected_location_names():
    return [
        "BEČVA ROŽNOVSKÁ 1",
        "BEČVA ROŽNOVSKÁ 2",
        "BEČVA VSETÍNSKÁ 1",
        "BEČVA VSETÍNSKÁ 2",
    ]


def get_expected_headquarters():
    return [
        "MO VALAŠSKÉ MEZIŘÍČÍ",
        "MO ROŽNOV POD RADHOŠTĚM",
        "MO VALAŠSKÉ MEZIŘÍČÍ",
        "MO VSETÍN",
    ]


def get_expected_area():
    return [
        8.0,
        27.4,
        16.0,
        22.0,
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
    ]
