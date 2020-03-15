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
    ]
