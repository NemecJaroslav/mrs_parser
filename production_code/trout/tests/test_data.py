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
        "463006",
        "463008",
        "463009",
        "463010",
        "463011",
        "463012",
        "463013",
        "463014",
        "463015",
        "463017",
        "463016",
        "463018",
        "463018",
        "463018",
        "463019",
        "463020",
        "463021",
    ]


def get_expected_location_names():
    return [
        "KŘTINSKÝ POTOK",
        "BĚLÁ BOSKOVICKÁ 1",
        "BESÉNEK 1",
        "BÍLÁ VODA",
     #   "BÍLÝ POTOK 1",
        "BÍLÝ POTOK 2",
        "BISKUPICKÝ POTOK 1",
        "BŘEZNICE 1",
        "BŘEZOVSKÝ POTOK 1",
        "BÝKOVKA 1",
        "BYSTŘICE HOSTÝNSKÁ 1",
        "BYSTŘICE PERNŠTEJNSKÁ 1",
        "CIKHÁJSKÝ POTOK 2",
        # TODO: SLUŠOVISKÁ vs SLUŠOVICKÁ
        "DŘEVNICE SLUŠOVICKÁ 1",
        "DŘEVNICE VIZOVICKÁ 1",
        "DYJE 12",
        "DYJE 12A",
        "DYJE 13/1",
        "DYJE 13/2",
        "DYJE 13/3",
        "DYJE 14",
        "DYJE 20",
        "FRYŠÁVKA 1",
    ]


def get_expected_headquarters():
    return [
        "ADAMOV",
        "BOSKOVICE",
        "TIŠNOV",
        "BLANSKO",
     #   "VEVERSKÁ BÍTÝŠKA",
        "VELKÁ BÍTEŠ",
        "UHERSKÝ BROD",
        "UHERSKÉ HRADIŠTĚ",
        "UHERSKÝ BROD",
        "BLANSKO",
        "BYSTŘICE POD HOSTÝNEM",
        "BYSTŘICE NAD PERNŠTEJNEM",
        "ŽĎÁR NAD SÁZAVOU",
        "ZLÍN",
        "ZLÍN",
        "ZNOJMO",
        "ZNOJMO",
        "ZNOJMO",
        "ZNOJMO",
        "ZNOJMO",
        "VRANOV NAD DYJÍ",
        "TELČ",
        "NOVÉ MĚSTO NA MORAVĚ",
    ]


def get_expected_area():
    return [
        2.0,
        4.2,
        5.0,
        4.0,
     #   1.5,
        9.3,
        3.0,
        4.0,
        2.0,
        3.0,
        2.0,
        5.0,
        1.0,
        4.0,
        20.0,
        49.0,
        12.0,
        17.0,
        8.0,
        11.0,
        22.0,
        2.2,
        5.0,
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
         (GPSCoordinate(49, 19, 03.80, "N"), GPSCoordinate(16, 10, 22.19, "E"))],
        [(GPSCoordinate(49, 4, 29.72, "N"), GPSCoordinate(17, 42, 48.26, "E")),
         (GPSCoordinate(49, 7, 14.97, "N"), GPSCoordinate(17, 41, 21.13, "E")),
         (GPSCoordinate(49, 4, 29.49, "N"), GPSCoordinate(17, 42, 48.39, "E")),
         (GPSCoordinate(49, 7, 20.47, "N"), GPSCoordinate(17, 43, 38.59, "E"))],
        [(GPSCoordinate(49, 5, 26.02, "N"), GPSCoordinate(17, 29, 47.70, "E")),
         (GPSCoordinate(49, 9, 48.60, "N"), GPSCoordinate(17, 38, 11.52, "E")),
         (GPSCoordinate(49, 6, 5.40, "N"), GPSCoordinate(17, 33, 13.35, "E")),
         (GPSCoordinate(49, 6, 22.15, "N"), GPSCoordinate(17, 35, 59.96, "E"))],
        [],
        [],
        [(GPSCoordinate(49, 25, 47.05, "N"), GPSCoordinate(17, 35, 46.56, "E")),
         (GPSCoordinate(49, 22, 41.05, "N"), GPSCoordinate(17, 43, 16.77, "E"))],
        [(GPSCoordinate(49, 33, 25.00, "N"), GPSCoordinate(16, 18, 55.74, "E")),
         (GPSCoordinate(49, 32, 40.30, "N"), GPSCoordinate(16, 12, 15.37, "E"))],
        [],
        [(GPSCoordinate(49, 13, 4.637, "N"), GPSCoordinate(17, 46, 40.884, "E")),
         (GPSCoordinate(49, 19, 13.154, "N"), GPSCoordinate(17, 46, 50.218, "E")),
         (GPSCoordinate(49, 19, 19.280, "N"), GPSCoordinate(17, 47, 33.645, "E")),
         (GPSCoordinate(49, 18, 10.76, "N"), GPSCoordinate(17, 45, 59.55, "E")),
         (GPSCoordinate(49, 17, 6.54, "N"), GPSCoordinate(17, 53, 31.36, "E")),
         (GPSCoordinate(49, 17, 55.52, "N"), GPSCoordinate(17, 50, 39.11, "E"))],
        [(GPSCoordinate(49, 13, 16.04, "N"), GPSCoordinate(17, 42, 54.71, "E")),
         (GPSCoordinate(49, 13, 16.77, "N"), GPSCoordinate(17, 50, 58.59, "E")),
         (GPSCoordinate(49, 13, 33.895, "N"), GPSCoordinate(17, 54, 49.109, "E")),
         (GPSCoordinate(49, 13, 16.8, "N"), GPSCoordinate(17, 50, 58.7, "E")),
         (GPSCoordinate(49, 14, 20.08, "N"), GPSCoordinate(17, 52, 56.90, "E")),
         (GPSCoordinate(49, 14, 27.47, "N"), GPSCoordinate(17, 44, 31.38, "E")),
         (GPSCoordinate(49, 11, 45.66, "N"), GPSCoordinate(17, 44, 31.26, "E"))],
        [],
        [(GPSCoordinate(48, 50, 19.722, "N"), GPSCoordinate(15, 59, 46.569, "E")),
         (GPSCoordinate(48, 49, 11.51, "N"), GPSCoordinate(15, 57, 34.93, "E"))],
        [(GPSCoordinate(48, 49, 33.51, "N"), GPSCoordinate(15, 56, 23.34, "E")),
         (GPSCoordinate(48, 50, 9.07, "N"), GPSCoordinate(15, 54, 22.22, "E"))],
        [(GPSCoordinate(48, 50, 56.69, "N"), GPSCoordinate(15, 53, 35.92, "E")),
         (GPSCoordinate(48, 51, 11.48, "N"), GPSCoordinate(15, 52, 51.71, "E"))],
        [(GPSCoordinate(48, 51, 29.53, "N"), GPSCoordinate(15, 52, 25.28, "E")),
         (GPSCoordinate(48, 51, 44.00, "N"), GPSCoordinate(15, 50, 32.73, "E"))],
        [(GPSCoordinate(48, 52, 32.77, "N"), GPSCoordinate(15, 50, 42.26, "E")),
         (GPSCoordinate(48, 54, 24.26, "N"), GPSCoordinate(15, 49, 9.81, "E"))],
        [(GPSCoordinate(49, 9, 38.65, "N"), GPSCoordinate(15, 28, 26.31, "E")),
         (GPSCoordinate(49, 12, 48.09, "N"), GPSCoordinate(15, 30, 44.30, "E"))],
        [(GPSCoordinate(49, 38, 19.68, "N"), GPSCoordinate(16, 13, 26.05, "E")),
         (GPSCoordinate(49, 37, 57.32, "N"), GPSCoordinate(16, 4, 30.65, "E"))],
    ]
