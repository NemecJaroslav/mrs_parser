from production_code.common.fishing_location import FishingLocation
from production_code.common.mrs_parser import GPSCoordinate


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
        "463001",
        "463002",
        "463003",
        "463004",
      #  "463032",
        "463005",
    ]


def get_expected_location_names():
    return [
        "KŘTINSKÝ POTOK",
        "BĚLÁ BOSKOVICKÁ 1",
        "BESÉNEK 1",
        "BÍLÁ VODA",
     #   "BÍLÝ POTOK 1",
        "BÍLÝ POTOK 2",
    ]


def get_expected_headquarters():
    return [
        "ADAMOV",
        "BOSKOVICE",
        "TIŠNOV",
        "BLANSKO",
     #   "VEVERSKÁ BÍTÝŠKA",
        "VELKÁ BÍTEŠ",
    ]


def get_expected_area():
    return [
        2.0,
        4.2,
        5.0,
        4.0,
     #   1.5,
        9.3,
    ]


def get_expected_gps():
    return [
        [],
        [(GPSCoordinate(49, 28, 19.30, "N"), GPSCoordinate(16, 37, 16.21, "E")),
         (GPSCoordinate(49, 29, 34.8, "N"), GPSCoordinate(16, 41, 51.60, "E"))],
        [],
        [],
        # [(GPSCoordinate(49, 16, 40.80, "N"), GPSCoordinate(16, 26, 16.99, "E")),
        #  (GPSCoordinate(49, 15, 44.85, "N"), GPSCoordinate(16, 23, 48.97, "E"))],
        [(GPSCoordinate(49, 15, 44.85, "N"), GPSCoordinate(16, 23, 48.97, "E")),
         (GPSCoordinate(49, 19, 03.80, "N"), GPSCoordinate(16, 10, 22.19, "E"))]
    ]
