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
        "471012",
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
        "471023",
        "471024",
        "471025",
        "471026",
        "471027",
        "471028",
        "471029",
        "471030",
        "471032",
        "471033",
        "471034",
        "471036",
        "471037",
        "471038",
        "471039",
        "471040",
        "471041",
        "471042",
        "471043",
        "471044",
        "471045",
        "471046",
        "471047",
        "471048",
        "471049",
        "471050",
        "471051",
        "471052",
        "471053",
        "471054",
        "471055",
        "471056",
        "471057",
        "471058",
        "471059",
        "471061",
        "471062",
        "471063",
        "471064",
        "471065",
        "471066",
        "471067",
        "471068",
        "471069",
        "471070",
        "471071",
        "471072",
        "471073",
        "471074",
        "471075",
        "471076",
        "471077",
        "471078",
        "471079",
        "471080",
        "471081",
        "471082",
        "471083",
        "471084",
        "471085",
        "471086",
        "471087",
        "471088",
        "471089",
        "471090",
        "471091",
        "471092",
        "471093",
        "471094",
        "471095",
        "471096",
        "471097",
        "471098",
        "471099",
        "471100",
        "471101",
        "471102",
        "471103",
        "471104",
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
        "BEČVA 5 A",
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
        "BYSTŘICE VALAŠSKÁ 1 A",
        "ČERNÝ POTOK 1 A",
        "ČIŽINA 1 A",
        "DESNÁ 1",
        "DESNÁ 1 A",
        "DUKELSKÉ NÁDRŽE 1 A",
        "HUSÍ POTOK 1 A",
        "CHOMOUTOV 1 A",
        "JIČÍNKA 1 A",
        "JUHYNĚ 1 A",
        "LAČNOVSKÝ POTOK 1 A",
        "LOUKY 1 A",
        "LUBINA 1",
        "LUBINA 2",
        "LUBINA 2 A",
        "LUBINA 4 A",
        "LUČINA 1",
        "LUČINA 1 A",
        "LUČINA 2 A",
        "MORAVA 14",
        "MORAVA 14 A",
        "MORAVA 15",
        "MORAVA 16",
        "MORAVA 17 A",
        "MORAVA 18",
        "MORAVA 19",
        "MORAVA 19 A",
        "MORAVA 20",
        "MORAVA 20 A",
        "MORAVA 21",
        "MORAVA 22",
        "MORAVA - OLOMOUCKÉ ŠTĚRKOVNY 1 A",
        "MORAVA STARÁ 1",
        "MORAVICE 1",
        "MORAVICE 3 A",
        "MOŠTĚNKA 1",
        "NEMILKA 1 A",
        "ODRA 1",
        "ODRA 1 A",
        "ODRA 2",
        "ODRA 2 A",
        "ODRA 3",
        "ODRA 3 A",
        "ODRA 4",
        "ODRA 4 A",
        "ODRA 5",
        "ODRA 5 A",
        "ODRA 6",
        "ODRA 6 A",
        "ODRA 7",
        "OLEŠNÁ 1",
        "OLEŠNÁ 2 A",
        "OLEŠNICE PŘEROVSKÁ 1",
        "OLŠE 1",
        "OLŠE 1 A",
        "OLŠE 2",
        "OLŠE 2 A",
        "OLŠE 3",
        "OLŠE 3 A",
        "OLŠE 4",
        "OLŠE 4 A",
        "OLŠE 5",
        "ONDŘEJNICE 1",
        "ONDŘEJNICE 1 A",
        "OPAVA 1",
        "OPAVA 2",
        "OPAVA 2 A",
        "OPAVA 3",
        "OPAVA 3 A",
        "OPAVA 4",
        "OPAVA 4 A",
        "OPAVA 5",
        "OPAVA 6",
        "OPAVA 6 A",
        "OPAVICE 1 A",
        "ORLOVSKÝ POTOK 1 A",
        "OSKAVA 1",
        "OSKAVA 2",
        "OSKAVA 2 A",
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
        "MO VSETÍN",
        "MO BRUNTÁL",
        "MO KRNOV",
        "MO ŠUMPERK",
        "MO ŠUMPERK",
        "MO HAVÍŘOV",
        "MO FULNEK",
        "MO OLOMOUC",
        "MO NOVÝ JIČÍN",
        "MO KELČ",
        "MO VSETÍN",
        "MO KARVINÁ",
        "MO JISTEBNÍK",
        "MO PŘÍBOR",
        "MO PŘÍBOR",
        "MO FRENŠTÁT POD RADHOŠTĚM",
        "MO OSTRAVA",
        "MO OSTRAVA",
        "MO LUČINA",
        "MO TOVAČOV",
        "MO TOVAČOV",
        "MO TOVAČOV",
        "MO TOVAČOV",
        "MO TOVAČOV",
        "MO OLOMOUC",
        "MO LITOVEL",
        "MO LITOVEL",
        "MO MOHELNICE",
        "MO MOHELNICE",
        "MO ZÁBŘEH",
        "MO ŠUMPERK",
        "MO OLOMOUC",
        "MO BRODEK U PŘEROVA",  # 32 vs 160 ascii after "U"
        "MO OPAVA",
        "MO VÍTKOV",
        "MO PŘEROV",
        "MO ZÁBŘEH NA MORAVĚ",  # 32 vs 160 ascii after "NA"
        "MO BOHUMÍN",
        "MO BOHUMÍN",
        "MO OSTRAVA",
        "MO OSTRAVA",
        "MO OSTRAVA",
        "MO OSTRAVA",
        "MO JISTEBNÍK",
        "MO JISTEBNÍK",
        "MO STUDÉNKA",
        "MO STUDÉNKA",
        "MO NOVÝ JIČÍN",
        "MO NOVÝ JIČÍN",
        "MO VÍTKOV",
        "MO PASKOV",
        "MO FRÝDEK-MÍSTEK",
        "MO BRODEK U PŘEROVA",  # 32 vs 160 ascii after "U"
        "MO BOHUMÍN",
        "MO BOHUMÍN",
        "MO KARVINÁ",
        "MO KARVINÁ",
        "MO KARVINÁ",
        "MO KARVINÁ",
        "MO ČESKÝ TĚŠÍN",
        "MO ČESKÝ TĚŠÍN",
        "MO TŘINEC",
        "MO STARÁ VES N. O.",
        "MO STARÁ VES N. O.",
        "MO OSTRAVA",
        "MO HLUČÍN",
        "MO HLUČÍN",
        "MO KRAVAŘE",
        "MO KRAVAŘE",
        "MO OPAVA",
        "MO OPAVA",
        "MO OPAVA",
        "MO KRNOV",
        "MO KRNOV",
        "MO KRNOV",
        "MO ORLOVÁ",
        "MO OLOMOUC",
        "MO ŠTERNBERK",
        "MO ŠTERNBERK",
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
        0.0,
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
        19.0,
        1.5,
        23.2,
        13.6,
        17.4,
        5.0,
        1.7,
        88.0,
        6.6,
        6.2,
        14.0,
        10.0,
        13.0,
        5.5,
        1.3,
        20.0,
        17.0,
        1.3,
        248.0,
        46.0,
        2.0,
        40.0,
        27.0,
        42.0,
        75.0,
        35.0,
        101.0,
        9.0,
        117.5,
        17.0,
        15.5,
        19.8,
        14.0,
        7.7,
        20.0,
        11.0,
        21.0,
        52.0,
        100.0,
        30.0,
        80.0,
        15.0,
        7.5,
        9.0,
        4.25,
        23.0,
        8.0,
        16.0,
        1.5,
        11.0,
        4.0,
        74.5,
        6.0,
        19.0,
        11.0,
        30.0,
        2.0,
        17.0,
        65.0,
        12.0,
        12.5,
        7.0,
        2.5,
        10.5,
        21.0,
        30.0,
        135.0,
        24.0,
        5.0,
        24.0,
        6.0,
        11.0,
        13.0,
        2.2,
        4.0,
        44.0,
        3.0,
        4.4,
        6.1,
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
        [],
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
        [(GPSCoordinate(49, 25, 25.211, "N"), GPSCoordinate(18, 1, 11.439, "E"))],
        [(GPSCoordinate(49, 59, 2.579, "N"), GPSCoordinate(17, 27, 45.154, "E"))],
        [(GPSCoordinate(50, 1, 13.101, "N"), GPSCoordinate(17, 46, 37.647, "E")),
         (GPSCoordinate(49, 57, 9.967, "N"), GPSCoordinate(17, 33, 14.271, "E")),
         (GPSCoordinate(50, 1, 47.276, "N"), GPSCoordinate(17, 43, 12.342, "E"))],
        [(GPSCoordinate(49, 54, 33.035, "N"), GPSCoordinate(16, 55, 48.18, "E")),
         (GPSCoordinate(49, 57, 11.594, "N"), GPSCoordinate(16, 59, 25.611, "E"))],
        [(GPSCoordinate(49, 54, 45.223, "N"), GPSCoordinate(16, 56, 28.182, "E")),
         (GPSCoordinate(49, 57, 53.359, "N"), GPSCoordinate(17, 1, 51.711, "E"))],
        [(GPSCoordinate(49, 48, 34.21, "N"), GPSCoordinate(18, 26, 7.484, "E"))],
        [(GPSCoordinate(49, 44, 0.754, "N"), GPSCoordinate(17, 54, 59.87, "E"))],
        [(GPSCoordinate(49, 39, 15.785, "N"), GPSCoordinate(17, 13, 50.404, "E"))],
        [(GPSCoordinate(49, 35, 49.668, "N"), GPSCoordinate(18, 1, 36.206, "E")),
         (GPSCoordinate(49, 34, 3.644, "N"), GPSCoordinate(17, 59, 58.986, "E")),
         (GPSCoordinate(49, 31, 37.502, "N"), GPSCoordinate(18, 1, 11.411, "E"))],
        [(GPSCoordinate(49, 28, 0.197, "N"), GPSCoordinate(17, 49, 4.754, "E")),
         (GPSCoordinate(49, 28, 0.473, "N"), GPSCoordinate(17, 48, 42.444, "E")),
         (GPSCoordinate(49, 28, 0.511, "N"), GPSCoordinate(17, 48, 41.204, "E")),
         (GPSCoordinate(49, 28, 0.076, "N"), GPSCoordinate(17, 48, 34.818, "E")),
         (GPSCoordinate(49, 28, 28.52, "N"), GPSCoordinate(17, 50, 18.871, "E"))],
        [(GPSCoordinate(49, 11, 6.757, "N"), GPSCoordinate(18, 3, 21.61, "E")),
         (GPSCoordinate(49, 11, 12.363, "N"), GPSCoordinate(18, 0, 46.351, "E")),
         (GPSCoordinate(49, 10, 48.137, "N"), GPSCoordinate(18, 2, 34.588, "E"))],
        [(GPSCoordinate(49, 48, 28.693, "N"), GPSCoordinate(18, 34, 22.164, "E"))],
        [(GPSCoordinate(49, 44, 47.018, "N"), GPSCoordinate(18, 10, 15.883, "E")),
         (GPSCoordinate(49, 41, 44.923, "N"), GPSCoordinate(18, 8, 16.767, "E"))],
        [(GPSCoordinate(49, 41, 44.621, "N"), GPSCoordinate(18, 8, 17.147, "E")),
         (GPSCoordinate(49, 39, 32.123, "N"), GPSCoordinate(18, 8, 31.392, "E"))],
        [(GPSCoordinate(49, 37, 42.102, "N"), GPSCoordinate(18, 10, 51.709, "E"))],
        [(GPSCoordinate(49, 37, 1.46, "N"), GPSCoordinate(18, 11, 11.804, "E"))],
        [(GPSCoordinate(49, 49, 55.067, "N"), GPSCoordinate(18, 17, 47.923, "E")),
         (GPSCoordinate(49, 46, 8.603, "N"), GPSCoordinate(18, 26, 0.94, "E"))],
        [(GPSCoordinate(49, 46, 44.566, "N"), GPSCoordinate(18, 22, 48.851, "E"))],
        [(GPSCoordinate(49, 44, 0.52, "N"), GPSCoordinate(18, 26, 54.268, "E"))],
        [(GPSCoordinate(49, 20, 17.263, "N"), GPSCoordinate(17, 20, 49.011, "E")),
         (GPSCoordinate(49, 23, 42.922, "N"), GPSCoordinate(17, 18, 18.294, "E")),
         (GPSCoordinate(49, 21, 14.153, "N"), GPSCoordinate(17, 19, 7.012, "E")),
         (GPSCoordinate(49, 23, 50.664, "N"), GPSCoordinate(17, 17, 37.496, "E"))],
        [(GPSCoordinate(49, 22, 12.282, "N"), GPSCoordinate(17, 18, 25.98, "E"))],
        [(GPSCoordinate(49, 23, 43.017, "N"), GPSCoordinate(17, 18, 18.373, "E")),
         (GPSCoordinate(49, 27, 56.205, "N"), GPSCoordinate(17, 18, 17.804, "E")),
         (GPSCoordinate(49, 23, 50.623, "N"), GPSCoordinate(17, 17, 37.097, "E")),
         (GPSCoordinate(49, 27, 56.554, "N"), GPSCoordinate(17, 17, 24.354, "E")),
         (GPSCoordinate(49, 25, 5.969, "N"), GPSCoordinate(17, 19, 16.072, "E")),
         (GPSCoordinate(49, 25, 54.128, "N"), GPSCoordinate(17, 20, 1.844, "E")),
         (GPSCoordinate(49, 28, 22.61, "N"), GPSCoordinate(17, 19, 8.269, "E"))],
        [(GPSCoordinate(49, 27, 56.681, "N"), GPSCoordinate(17, 18, 17.454, "E")),
         (GPSCoordinate(49, 30, 42.676, "N"), GPSCoordinate(17, 15, 38.985, "E")),
         (GPSCoordinate(49, 27, 56.809, "N"), GPSCoordinate(17, 17, 23.77, "E")),
         (GPSCoordinate(49, 29, 45.844, "N"), GPSCoordinate(17, 16, 30.785, "E"))],
        [(GPSCoordinate(49, 25, 18.135, "N"), GPSCoordinate(17, 18, 15.11, "E"))],
        [(GPSCoordinate(49, 30, 42.89, "N"), GPSCoordinate(17, 15, 38.845, "E")),
         (GPSCoordinate(49, 41, 32.373, "N"), GPSCoordinate(17, 8, 12.705, "E")),
         (GPSCoordinate(49, 34, 58.187, "N"), GPSCoordinate(17, 15, 41.028, "E")),
         (GPSCoordinate(49, 40, 55.607, "N"), GPSCoordinate(17, 7, 15.144, "E")),
         (GPSCoordinate(49, 32, 4.915, "N"), GPSCoordinate(17, 16, 13.904, "E")),
         (GPSCoordinate(49, 31, 47.455, "N"), GPSCoordinate(17, 16, 50.312, "E")),
         (GPSCoordinate(49, 41, 6.093, "N"), GPSCoordinate(17, 8, 42.523, "E")),
         (GPSCoordinate(49, 41, 20.43, "N"), GPSCoordinate(17, 7, 16.874, "E")),
         (GPSCoordinate(49, 37, 8.766, "N"), GPSCoordinate(17, 15, 25.115, "E")),
         (GPSCoordinate(49, 39, 14.679, "N"), GPSCoordinate(17, 16, 41.073, "E")),
         (GPSCoordinate(49, 35, 10.4172, "N"), GPSCoordinate(17, 15, 43.1892, "E")),
         (GPSCoordinate(49, 33, 48.4164, "N"), GPSCoordinate(17, 15, 54.9792, "E"))],
        [(GPSCoordinate(49, 41, 32.407, "N"), GPSCoordinate(17, 8, 12.657, "E")),
         (GPSCoordinate(49, 44, 7.169, "N"), GPSCoordinate(16, 59, 29.486, "E")),
         (GPSCoordinate(49, 40, 55.948, "N"), GPSCoordinate(17, 7, 14.236, "E")),
         (GPSCoordinate(49, 42, 42.507, "N"), GPSCoordinate(17, 0, 49.746, "E")),
         (GPSCoordinate(49, 42, 3.124, "N"), GPSCoordinate(17, 3, 7.368, "E")),
         (GPSCoordinate(49, 43, 12.086, "N"), GPSCoordinate(17, 0, 4.144, "E")),
         (GPSCoordinate(49, 41, 20.384, "N"), GPSCoordinate(17, 7, 16.747, "E")),
         (GPSCoordinate(49, 41, 15.095, "N"), GPSCoordinate(17, 6, 33.889, "E")),
         (GPSCoordinate(49, 41, 46.948, "N"), GPSCoordinate(17, 7, 43.615, "E")),
         (GPSCoordinate(49, 42, 41.263, "N"), GPSCoordinate(17, 5, 49.63, "E")),
         (GPSCoordinate(49, 41, 51.245, "N"), GPSCoordinate(17, 4, 22.504, "E")),
         (GPSCoordinate(49, 41, 45.531, "N"), GPSCoordinate(17, 4, 38.636, "E")),
         (GPSCoordinate(49, 42, 3.643, "N"), GPSCoordinate(17, 3, 41.99, "E")),
         (GPSCoordinate(49, 42, 10.714, "N"), GPSCoordinate(17, 3, 14.004, "E")),
         (GPSCoordinate(49, 43, 24.082, "N"), GPSCoordinate(16, 59, 53.023, "E"))],
        [(GPSCoordinate(49, 39, 55.56, "N"), GPSCoordinate(17, 8, 3.123, "E"))],
        [(GPSCoordinate(49, 44, 7.218, "N"), GPSCoordinate(16, 59, 29.438, "E")),
         (GPSCoordinate(49, 48, 24.553, "N"), GPSCoordinate(16, 56, 16.419, "E"))],
        [(GPSCoordinate(49, 47, 1.409, "N"), GPSCoordinate(16, 57, 16.242, "E")),
         (GPSCoordinate(49, 46, 51.763, "N"), GPSCoordinate(16, 57, 15.529, "E")),
         (GPSCoordinate(49, 45, 54.669, "N"), GPSCoordinate(16, 57, 29.581, "E")),
         (GPSCoordinate(49, 46, 12.454, "N"), GPSCoordinate(16, 57, 23.448, "E")),
         (GPSCoordinate(49, 45, 46.405, "N"), GPSCoordinate(16, 54, 10.831, "E"))],
        [(GPSCoordinate(49, 48, 24.706, "N"), GPSCoordinate(16, 56, 16.926, "E")),
         (GPSCoordinate(49, 54, 32.796, "N"), GPSCoordinate(16, 55, 47.97, "E"))],
        [(GPSCoordinate(49, 54, 32.832, "N"), GPSCoordinate(16, 55, 47.746, "E")),
         (GPSCoordinate(49, 56, 32.188, "N"), GPSCoordinate(16, 54, 0.168, "E"))],
        [(GPSCoordinate(49, 33, 54.261, "N"), GPSCoordinate(17, 16, 40.76, "E")),
         (GPSCoordinate(49, 33, 53.522, "N"), GPSCoordinate(17, 16, 36.755, "E")),
         (GPSCoordinate(49, 33, 55.812, "N"), GPSCoordinate(17, 16, 4.286, "E")),
         (GPSCoordinate(49, 32, 42.155, "N"), GPSCoordinate(17, 16, 4.955, "E")),
         (GPSCoordinate(49, 37, 9.109, "N"), GPSCoordinate(17, 14, 55.46, "E")),
         (GPSCoordinate(49, 37, 29.392, "N"), GPSCoordinate(17, 15, 2.813, "E")),
         (GPSCoordinate(49, 37, 29.392, "N"), GPSCoordinate(17, 15, 2.813, "E")),
         (GPSCoordinate(49, 37, 29.392, "N"), GPSCoordinate(17, 15, 2.813, "E")),
         (GPSCoordinate(49, 38, 13.213, "N"), GPSCoordinate(17, 16, 7.263, "E")),
         (GPSCoordinate(49, 39, 35.008, "N"), GPSCoordinate(17, 10, 1.878, "E"))],
        [(GPSCoordinate(49, 28, 22.61, "N"), GPSCoordinate(17, 19, 8.269, "E")),
         (GPSCoordinate(49, 31, 47.438, "N"), GPSCoordinate(17, 16, 50.361, "E")),
         (GPSCoordinate(49, 31, 5.522, "N"), GPSCoordinate(17, 19, 18.113, "E"))],
        [(GPSCoordinate(49, 55, 38.301, "N"), GPSCoordinate(17, 56, 44.973, "E")),
         (GPSCoordinate(49, 54, 22.567, "N"), GPSCoordinate(17, 54, 29.65, "E")),
         (GPSCoordinate(49, 54, 25.506, "N"), GPSCoordinate(17, 54, 32.246, "E"))],
        [(GPSCoordinate(49, 48, 27.654, "N"), GPSCoordinate(17, 45, 55.627, "E")),
         (GPSCoordinate(49, 48, 49.165, "N"), GPSCoordinate(17, 44, 54.143, "E"))],
        [(GPSCoordinate(49, 19, 37.11, "N"), GPSCoordinate(17, 23, 9.41, "E")),
         (GPSCoordinate(49, 25, 43.677, "N"), GPSCoordinate(17, 30, 45.513, "E")),
         (GPSCoordinate(49, 27, 56.653, "N"), GPSCoordinate(17, 34, 59.817, "E"))],
        [(GPSCoordinate(49, 52, 19.227, "N"), GPSCoordinate(16, 50, 13.661, "E"))],
        [(GPSCoordinate(49, 56, 56.061, "N"), GPSCoordinate(18, 19, 58.859, "E")),
         (GPSCoordinate(49, 52, 18.028, "N"), GPSCoordinate(18, 17, 6.923, "E")),
         (GPSCoordinate(49, 56, 2.339, "N"), GPSCoordinate(18, 21, 3.617, "E")),
         (GPSCoordinate(49, 52, 5.086, "N"), GPSCoordinate(18, 20, 45.398, "E")),
         (GPSCoordinate(49, 53, 50.325, "N"), GPSCoordinate(18, 19, 13.355, "E")),
         (GPSCoordinate(49, 52, 4.959, "N"), GPSCoordinate(18, 20, 45.289, "E")),
         (GPSCoordinate(49, 55, 45.262, "N"), GPSCoordinate(18, 20, 59.447, "E"))],
        [(GPSCoordinate(49, 53, 27.346, "N"), GPSCoordinate(18, 19, 28.007, "E"))],
        [(GPSCoordinate(49, 52, 17.775, "N"), GPSCoordinate(18, 17, 6.154, "E")),
         (GPSCoordinate(49, 48, 45.382, "N"), GPSCoordinate(18, 13, 3.596, "E"))],
        [(GPSCoordinate(49, 51, 34.671, "N"), GPSCoordinate(18, 15, 3.187, "E")),
         (GPSCoordinate(49, 48, 32.926, "N"), GPSCoordinate(18, 12, 59.740, "E")),
         (GPSCoordinate(49, 48, 27.496, "N"), GPSCoordinate(18, 13, 2.848, "E")),
         (GPSCoordinate(49, 48, 32.960, "N"), GPSCoordinate(18, 13, 24.251, "E")),
         (GPSCoordinate(49, 53, 49.816, "N"), GPSCoordinate(18, 18, 59.757, "E")),
         (GPSCoordinate(49, 54, 23.588, "N"), GPSCoordinate(18, 19, 13.359, "E")),
         (GPSCoordinate(49, 48, 12.351, "N"), GPSCoordinate(18, 12, 53.967, "E"))],
        [(GPSCoordinate(49, 48, 45.317, "N"), GPSCoordinate(18, 13, 3.616, "E")),
         (GPSCoordinate(49, 44, 47.518, "N"), GPSCoordinate(18, 10, 15.366, "E")),
         (GPSCoordinate(49, 46, 0.042, "N"), GPSCoordinate(18, 11, 24.63, "E")),
         (GPSCoordinate(49, 47, 0.86, "N"), GPSCoordinate(18, 8, 24.851, "E"))],
        [(GPSCoordinate(49, 48, 25.176, "N"), GPSCoordinate(18, 13, 28.454, "E")),
         (GPSCoordinate(49, 47, 24.144, "N"), GPSCoordinate(18, 13, 6.237, "E")),
         (GPSCoordinate(49, 45, 17.094, "N"), GPSCoordinate(18, 10, 51.599, "E"))],
        [(GPSCoordinate(49, 44, 47.487, "N"), GPSCoordinate(18, 10, 15.289, "E")),
         (GPSCoordinate(49, 43, 23.06, "N"), GPSCoordinate(18, 7, 49.825, "E"))],
        [(GPSCoordinate(49, 44, 26.385, "N"), GPSCoordinate(18, 9, 34.206, "E")),
         (GPSCoordinate(49, 44, 31.257, "N"), GPSCoordinate(18, 9, 43.768, "E")),
         (GPSCoordinate(49, 44, 34.315, "N"), GPSCoordinate(18, 9, 51.264, "E")),
         (GPSCoordinate(49, 43, 12.739, "N"), GPSCoordinate(18, 7, 12.844, "E"))],
        [(GPSCoordinate(49, 43, 22.911, "N"), GPSCoordinate(18, 7, 49.941, "E")),
         (GPSCoordinate(49, 39, 56.899, "N"), GPSCoordinate(17, 59, 32.684, "E"))],
        [(GPSCoordinate(49, 42, 39.203, "N"), GPSCoordinate(18, 5, 29.603, "E")),
         (GPSCoordinate(49, 42, 44.383, "N"), GPSCoordinate(18, 5, 46.04, "E")),
         (GPSCoordinate(49, 42, 42.41, "N"), GPSCoordinate(18, 6, 0.162, "E")),
         (GPSCoordinate(49, 43, 8.109, "N"), GPSCoordinate(18, 7, 2.905, "E"))],
        [(GPSCoordinate(49, 39, 56.938, "N"), GPSCoordinate(17, 59, 32.461, "E")),
         (GPSCoordinate(49, 37, 27.371, "N"), GPSCoordinate(17, 54, 34.776, "E"))],
        [(GPSCoordinate(49, 39, 58.589, "N"), GPSCoordinate(17, 54, 30.54, "E"))],
        [(GPSCoordinate(49, 37, 27.439, "N"), GPSCoordinate(17, 54, 34.631, "E")),
         (GPSCoordinate(49, 41, 2.198, "N"), GPSCoordinate(17, 48, 4.232, "E")),
         (GPSCoordinate(49, 41, 38.011, "N"), GPSCoordinate(17, 49, 42.037, "E"))],
        [(GPSCoordinate(49, 44, 41.176, "N"), GPSCoordinate(18, 17, 44.934, "E")),
         (GPSCoordinate(49, 42, 9.458, "N"), GPSCoordinate(18, 18, 7.366, "E"))],
        [],
        [(GPSCoordinate(49, 28, 57.243, "N"), GPSCoordinate(17, 18, 49.053, "E")),
         (GPSCoordinate(49, 30, 59.912, "N"), GPSCoordinate(17, 25, 21.586, "E")),
         (GPSCoordinate(49, 29, 53.28, "N"), GPSCoordinate(17, 22, 37.638, "E"))],
        [(GPSCoordinate(49, 56, 56.561, "N"), GPSCoordinate(18, 20, 0.048, "E")),
         (GPSCoordinate(49, 54, 41.78, "N"), GPSCoordinate(18, 28, 39.384, "E"))],
        [],
        [(GPSCoordinate(49, 54, 41.746, "N"), GPSCoordinate(18, 28, 39.457, "E")),
         (GPSCoordinate(49, 50, 26.188, "N"), GPSCoordinate(18, 33, 24.296, "E"))],
        [(GPSCoordinate(49, 53, 32.432, "N"), GPSCoordinate(18, 29, 15.581, "E"))],
        [(GPSCoordinate(49, 53, 32.432, "N"), GPSCoordinate(18, 33, 25.656, "E")),
         (GPSCoordinate(49, 48, 28.277, "N"), GPSCoordinate(18, 35, 0.246, "E"))],
        [(GPSCoordinate(49, 53, 5.86, "N"), GPSCoordinate(18, 29, 46.599, "E")),
         (GPSCoordinate(49, 51, 2.43, "N"), GPSCoordinate(18, 31, 53.91, "E")),
         (GPSCoordinate(49, 51, 2.43, "N"), GPSCoordinate(18, 31, 53.91, "E"))],
        [(GPSCoordinate(49, 48, 28.211, "N"), GPSCoordinate(18, 35, 0.291, "E")),
         (GPSCoordinate(49, 42, 57.299, "N"), GPSCoordinate(18, 37, 43.798, "E"))],
        [(GPSCoordinate(49, 43, 33.665, "N"), GPSCoordinate(18, 37, 28.575, "E")),
         (GPSCoordinate(49, 43, 39.422, "N"), GPSCoordinate(18, 37, 28.579, "E")),
         (GPSCoordinate(49, 44, 50.878, "N"), GPSCoordinate(18, 36, 17.754, "E"))],
        [(GPSCoordinate(49, 42, 56.727, "N"), GPSCoordinate(18, 37, 43.955, "E")),
         (GPSCoordinate(49, 41, 4.012, "N"), GPSCoordinate(18, 39, 6.612, "E"))],
        [(GPSCoordinate(49, 45, 11.151, "N"), GPSCoordinate(18, 10, 54.1, "E")),
         (GPSCoordinate(49, 43, 16.326, "N"), GPSCoordinate(18, 11, 41.415, "E"))],
        [(GPSCoordinate(49, 44, 32.603, "N"), GPSCoordinate(18, 11, 8.419, "E")),
         (GPSCoordinate(49, 40, 3.899, "N"), GPSCoordinate(18, 15, 24.083, "E")),
         (GPSCoordinate(49, 42, 19.095, "N"), GPSCoordinate(18, 13, 58.452, "E")),
         (GPSCoordinate(49, 42, 18.06, "N"), GPSCoordinate(18, 13, 39.556, "E"))],
        [(GPSCoordinate(49, 50, 0.944, "N"), GPSCoordinate(18, 13, 16.4, "E")),
         (GPSCoordinate(49, 53, 11.414, "N"), GPSCoordinate(18, 10, 0.377, "E"))],
        [(GPSCoordinate(49, 53, 11.465, "N"), GPSCoordinate(18, 10, 0.28, "E")),
         (GPSCoordinate(49, 54, 25.72, "N"), GPSCoordinate(18, 4, 3.15, "E")),
         (GPSCoordinate(49, 54, 26.894, "N"), GPSCoordinate(18, 4, 2.221, "E")),
         (GPSCoordinate(49, 54, 13.885, "N"), GPSCoordinate(18, 7, 31.477, "E")),
         (GPSCoordinate(49, 54, 16.091, "N"), GPSCoordinate(18, 6, 49.849, "E")),
         (GPSCoordinate(49, 54, 18.849, "N"), GPSCoordinate(18, 5, 33.478, "E"))],
        [(GPSCoordinate(49, 53, 28.963, "N"), GPSCoordinate(18, 10, 40.179, "E"))],
        [(GPSCoordinate(49, 54, 25.738, "N"), GPSCoordinate(18, 4, 3.05, "E")),
         (GPSCoordinate(49, 55, 7.406, "N"), GPSCoordinate(17, 59, 21.717, "E"))],
        [(GPSCoordinate(49, 55, 17.159, "N"), GPSCoordinate(18, 2, 50.996, "E")),
         (GPSCoordinate(49, 55, 11.186, "N"), GPSCoordinate(18, 2, 43.547, "E")),
         (GPSCoordinate(49, 55, 9.093, "N"), GPSCoordinate(18, 4, 34.32, "E")),
         (GPSCoordinate(49, 55, 31.034, "N"), GPSCoordinate(17, 59, 54.834, "E")),
         (GPSCoordinate(49, 54, 25.855, "N"), GPSCoordinate(18, 4, 24.321, "E")),
         (GPSCoordinate(49, 54, 23.451, "N"), GPSCoordinate(18, 3, 54.631, "E")),
         (GPSCoordinate(49, 54, 15.102, "N"), GPSCoordinate(18, 4, 42.04, "E"))],
        [(GPSCoordinate(49, 55, 7.377, "N"), GPSCoordinate(17, 59, 21.59, "E")),
         (GPSCoordinate(49, 58, 0.559, "N"), GPSCoordinate(17, 52, 39.954, "E"))],
        [(GPSCoordinate(49, 57, 13.771, "N"), GPSCoordinate(17, 53, 39.732, "E"))],
        [(GPSCoordinate(49, 58, 0.625, "N"), GPSCoordinate(17, 52, 39.908, "E")),
         (GPSCoordinate(50, 1, 9.083, "N"), GPSCoordinate(17, 47, 12.825, "E")),
         (GPSCoordinate(50, 0, 26.637, "N"), GPSCoordinate(17, 48, 9.501, "E"))],
        [(GPSCoordinate(50, 1, 9.198, "N"), GPSCoordinate(17, 47, 12.756, "E")),
         (GPSCoordinate(50, 5, 0.723, "N"), GPSCoordinate(17, 44, 10.98, "E"))],
        [(GPSCoordinate(50, 1, 24.875, "N"), GPSCoordinate(17, 38, 21.114, "E")),
         (GPSCoordinate(50, 6, 28.078, "N"), GPSCoordinate(17, 38, 45.419, "E"))],
        [(GPSCoordinate(50, 9, 45.735, "N"), GPSCoordinate(17, 35, 30.854, "E"))],
        [(GPSCoordinate(49, 52, 4.939, "N"), GPSCoordinate(18, 20, 45.413, "E")),
         (GPSCoordinate(49, 50, 56.724, "N"), GPSCoordinate(18, 25, 32.45, "E")),
         (GPSCoordinate(49, 49, 49.166, "N"), GPSCoordinate(18, 25, 42.13, "E")),
         (GPSCoordinate(49, 49, 40.057, "N"), GPSCoordinate(18, 26, 37.212, "E")),
         (GPSCoordinate(49, 50, 17.594, "N"), GPSCoordinate(18, 26, 47.355, "E")),
         (GPSCoordinate(49, 50, 9.548, "N"), GPSCoordinate(18, 27, 17.705, "E")),
         (GPSCoordinate(49, 51, 29.379, "N"), GPSCoordinate(18, 27, 22.877, "E")),
         (GPSCoordinate(49, 51, 10.371, "N"), GPSCoordinate(18, 27, 53.067, "E"))],
        [(GPSCoordinate(49, 37, 55.514, "N"), GPSCoordinate(17, 14, 45.12, "E")),
         (GPSCoordinate(49, 41, 30.331, "N"), GPSCoordinate(17, 12, 38.388, "E")),
         (GPSCoordinate(49, 40, 40.927, "N"), GPSCoordinate(17, 14, 7.051, "E")),
         (GPSCoordinate(49, 44, 56.403, "N"), GPSCoordinate(17, 12, 7.196, "E"))],
        [(GPSCoordinate(49, 41, 30.447, "N"), GPSCoordinate(17, 12, 38.269, "E")),
         (GPSCoordinate(49, 43, 18.346, "N"), GPSCoordinate(17, 9, 29.735, "E")),
         (GPSCoordinate(49, 42, 31.835, "N"), GPSCoordinate(17, 11, 30.819, "E")),
         (GPSCoordinate(49, 47, 5.397, "N"), GPSCoordinate(17, 11, 40.259, "E"))],
        [(GPSCoordinate(49, 43, 11.019, "N"), GPSCoordinate(17, 16, 41.579, "E")),
         (GPSCoordinate(49, 46, 2.103, "N"), GPSCoordinate(17, 11, 48.775, "E")),
         (GPSCoordinate(49, 47, 29.176, "N"), GPSCoordinate(17, 12, 40.661, "E")),
         (GPSCoordinate(49, 41, 15.143, "N"), GPSCoordinate(17, 17, 9.728, "E"))],
    ]
