from production_code.common.fishing_location import FishingLocation
from production_code.common.parser import GPSCoordinate


def get_expected_fishing_locations():
    return [
        FishingLocation("473001", "BEČVA ROŽNOVSKÁ 1", "MO VALAŠSKÉ MEZIŘÍČÍ", 0.0,
                        [(GPSCoordinate(49, 28, 26.990, "N"), GPSCoordinate(17, 59, 36.268, "E")),
                         (GPSCoordinate(49, 27, 50.564, "N"), GPSCoordinate(18, 3, 15.331, "E"))]),
        FishingLocation("473002", "BEČVA ROŽNOVSKÁ 2", "MO ROŽNOV POD RADHOŠTĚM", 0.0,
                        [(GPSCoordinate(49, 27, 50.284, "N"), GPSCoordinate(18, 3, 14.53, "E")),
                         (GPSCoordinate(49, 25, 21.042, "N"), GPSCoordinate(18, 18, 50.902, "E")),
                         (GPSCoordinate(49, 27, 50.564, "N"), GPSCoordinate(18, 3, 15.331, "E")),
                         (GPSCoordinate(49, 24, 20.332, "N"), GPSCoordinate(18, 21, 47.065, "E")),
                         (GPSCoordinate(49, 25, 24.142, "N"), GPSCoordinate(18, 19, 5.337, "E"))]),
        FishingLocation("473003", "BEČVA VSETÍNSKÁ 1", "MO VALAŠSKÉ MEZIŘÍČÍ", 0.0,
                        [(GPSCoordinate(49, 28, 12.2, "N"), GPSCoordinate(17, 57, 16.0, "E")),
                         (GPSCoordinate(49, 25, 9.252, "N"), GPSCoordinate(17, 57, 35.725, "E"))]),
        FishingLocation("473004", "BEČVA VSETÍNSKÁ 2", "MO VSETÍN", 0.0,
                        [(GPSCoordinate(49, 25, 9.397, "N"), GPSCoordinate(17, 57, 34.989, "E")),
                         (GPSCoordinate(49, 19, 28.692, "N"), GPSCoordinate(17, 59, 48.081, "E"))]),
        FishingLocation("473005", "BEČVA VSETÍNSKÁ 3", "MO VSETÍN", 0.0,
                        [(GPSCoordinate(49, 19, 28.692, "N"), GPSCoordinate(17, 59, 48.081, "E")),
                         (GPSCoordinate(49, 19, 32.139, "N"), GPSCoordinate(18, 9, 46.821, "E"))]),
        FishingLocation("473006", "BEČVA VSETÍNSKÁ 4 P", "MO VSETÍN", 0.0,
                        [(GPSCoordinate(49, 19, 32.139, "N"), GPSCoordinate(18, 9, 46.821, "E")),
                         (GPSCoordinate(49, 23, 50.365, "N"), GPSCoordinate(18, 23, 53.459, "E"))]),
        FishingLocation("473007", "BĚLÁ JESENICKÁ 1", "MO JESENÍK", 0.0,
                        [(GPSCoordinate(50, 18, 24.265, "N"), GPSCoordinate(17, 21, 11.726, "E")),
                         (GPSCoordinate(50, 14, 1.308, "N"), GPSCoordinate(17, 12, 20.890, "E"))]),
        FishingLocation("473008", "BĚLÁ JESENICKÁ 2", "MO JESENÍK", 0.0,
                        [(GPSCoordinate(50, 14, 1.308, "N"), GPSCoordinate(17, 12, 20.890, "E")),
                         (GPSCoordinate(50, 6, 54.785, "N"), GPSCoordinate(17, 14, 32.321, "E"))]),
        FishingLocation("473009", "BÍLOVKA 1", "MO BÍLOVEC", 0.0,
                        [(GPSCoordinate(49, 43, 34.946, "N"), GPSCoordinate(18, 8, 3.449, "E")),
                         (GPSCoordinate(49, 43, 47.495, "N"), GPSCoordinate(18, 8, 22.678, "E")),
                         (GPSCoordinate(49, 47, 32.788, "N"), GPSCoordinate(17, 54, 28.153, "E")),
                         (GPSCoordinate(49, 45, 45.290, "N"), GPSCoordinate(17, 59, 31.794, "E"))]),
        FishingLocation("473010", "BRANNÁ 1", "MO ŠUMPERK", 0.0,
                        [(GPSCoordinate(50, 4, 35.876, "N"), GPSCoordinate(16, 56, 4.887, "E")),
                         (GPSCoordinate(50, 13, 38.054, "N"), GPSCoordinate(17, 1, 44.841, "E"))]),
        FishingLocation("473011", "BŘEZNÁ 1", "MO ZÁBŘEH NA MORAVĚ", 0.0,
                        [(GPSCoordinate(49, 52, 27.024, "N"), GPSCoordinate(16, 46, 10.188, "E")),
                         (GPSCoordinate(49, 57, 28.469, "N"), GPSCoordinate(16, 45, 52.546, "E"))]),
        FishingLocation("473012", "BŘEZNÁ 2", "MO ZÁBŘEH NA MORAVĚ", 0.0,
                        [(GPSCoordinate(49, 57, 28.469, "N"), GPSCoordinate(16, 45, 52.546, "E")),
                         (GPSCoordinate(50, 3, 0.436, "N"), GPSCoordinate(16, 50, 45.244, "E"))]),
        FishingLocation("473013", "BUDIŠOVKA 1 P", "MO VÍTKOV", 0.0,
                        [(GPSCoordinate(49, 44, 6.875, "N"), GPSCoordinate(17, 41, 38.043, "E")),
                         (GPSCoordinate(49, 46, 55.517, "N"), GPSCoordinate(17, 32, 7.460, "E"))]),
        FishingLocation("473014", "BYSTŘICE HANÁCKÁ 2 P", "MO VELKÁ BYSTŘICE", 0.0,
                        [(GPSCoordinate(49, 35, 38.112, "N"), GPSCoordinate(17, 19, 52.902, "E")),
                         (GPSCoordinate(49, 39, 15.305, "N"), GPSCoordinate(17, 24, 38.199, "E"))]),
        FishingLocation("473015", "BYSTŘICE HANÁCKÁ 3", "MO DOMAŠOV NAD BYSTŘICÍ", 0.0,
                        [(GPSCoordinate(49, 39, 15.305, "N"), GPSCoordinate(17, 24, 38.199, "E")),
                         (GPSCoordinate(49, 44, 48.566, "N"), GPSCoordinate(17, 26, 14.758, "E")),
                         (GPSCoordinate(49, 44, 56.370, "N"), GPSCoordinate(17, 27, 21.840, "E")),
                         (GPSCoordinate(49, 45, 2.316, "N"), GPSCoordinate(17, 27, 21.869, "E"))]),
        FishingLocation("473016", "BYSTŘICE HANÁCKÁ 4", "MO DOMAŠOV NAD BYSTŘICÍ", 0.0,
                        [(GPSCoordinate(49, 44, 48.566, "N"), GPSCoordinate(17, 26, 14.758, "E")),
                         (GPSCoordinate(49, 50, 2.843, "N"), GPSCoordinate(17, 24, 2.666, "E")),
                         (GPSCoordinate(49, 46, 51.140, "N"), GPSCoordinate(17, 26, 29.589, "E")),
                         (GPSCoordinate(49, 47, 51.232, "N"), GPSCoordinate(17, 26, 44.956, "E")),
                         (GPSCoordinate(49, 47, 52.460, "N"), GPSCoordinate(17, 25, 16.512, "E"))]),
        FishingLocation("473017", "BYSTŘICE VALAŠSKÁ 1 P", "MO VSETÍN", 0.0,
                        [(GPSCoordinate(49, 25, 11.500, "N"), GPSCoordinate(17, 57, 50.776, "E")),
                         (GPSCoordinate(49, 23, 3.192, "N"), GPSCoordinate(18, 11, 15.288, "E"))]),
        FishingLocation("473018", "ČELADENKA 1", "MO FRÝDLANT NAD OSTRAVICÍ", 0.0,
                        [(GPSCoordinate(49, 34, 6.847, "N"), GPSCoordinate(18, 21, 46.536, "E")),
                         (GPSCoordinate(49, 27, 11.437, "N"), GPSCoordinate(18, 22, 13.214, "E")),
                         (GPSCoordinate(49, 34, 3.781, "N"), GPSCoordinate(18, 21, 18.105, "E")),
                         (GPSCoordinate(49, 34, 4.695, "N"), GPSCoordinate(18, 21, 31.439, "E"))]),
        FishingLocation("473019", "ČERNÁ OPAVA 1", "MO VRBNO POD PRADĚDEM", 0.0,
                        [(GPSCoordinate(50, 7, 32.728, "N"), GPSCoordinate(17, 22, 46.621, "E")),
                         (GPSCoordinate(50, 10, 44.479, "N"), GPSCoordinate(17, 17, 23.541, "E"))]),
        FishingLocation("473021", "ČERVENÝ POTOK 1", "MO JAVORNÍK", 0.0,
                        [(GPSCoordinate(50, 21, 46.267, "N"), GPSCoordinate(17, 9, 54.474, "E")),
                         (GPSCoordinate(50, 16, 50.763, "N"), GPSCoordinate(17, 10, 34.332, "E")),
                         (GPSCoordinate(50, 20, 41.036, "N"), GPSCoordinate(17, 10, 34.112, "E")),
                         (GPSCoordinate(50, 18, 54.629, "N"), GPSCoordinate(17, 9, 41.606, "E"))]),
        FishingLocation("473022", "HOŘINA 1", "MO KRNOV", 0.0,
                        [(GPSCoordinate(50, 1, 10.1, "N"), GPSCoordinate(17, 46, 23.8, "E")),
                         (GPSCoordinate(49, 58, 51.2, "N"), GPSCoordinate(17, 39, 0.9, "E"))]),
        FishingLocation("473023", "DESNÁ 2", "MO ŠUMPERK", 0.0,
                        [(GPSCoordinate(49, 57, 17.675, "N"), GPSCoordinate(16, 59, 26.886, "E")),
                         (GPSCoordinate(50, 4, 9.797, "N"), GPSCoordinate(17, 5, 13.442, "E"))]),
        FishingLocation("473024", "DESNÁ 3", "MO ŠUMPERK", 0.0,
                        [(GPSCoordinate(50, 4, 9.797, "N"), GPSCoordinate(17, 5, 13.442, "E")),
                         (GPSCoordinate(50, 3, 16.704, "N"), GPSCoordinate(17, 13, 22.508, "E")),
                         (GPSCoordinate(50, 5, 57.016, "N"), GPSCoordinate(17, 6, 26.266, "E")),
                         (GPSCoordinate(50, 9, 33.902, "N"), GPSCoordinate(17, 6, 47.796, "E"))]),
        FishingLocation("473025", "HERLIČKA 1", "MO OPAVA", 0.0,
                        [(GPSCoordinate(49, 59, 33.371, "N"), GPSCoordinate(17, 49, 18.173, "E")),
                         (GPSCoordinate(49, 58, 26.762, "N"), GPSCoordinate(17, 39, 28.058, "E"))]),
        FishingLocation("473026", "HLUCHOVÁ 1", "MO BYSTŘICE NAD OLŠÍ", 0.0,
                        [(GPSCoordinate(49, 37, 52.722, "N"), GPSCoordinate(18, 43, 0.940, "E")),
                         (GPSCoordinate(49, 36, 24.616, "N"), GPSCoordinate(18, 49, 15.938, "E"))]),
        FishingLocation("473027", "HROZOVÁ 1", "MO KRNOV", 0.0,
                        [(GPSCoordinate(50, 14, 41.915, "N"), GPSCoordinate(17, 43, 5.125, "E")),
                         (GPSCoordinate(50, 10, 45.570, "N"), GPSCoordinate(17, 36, 27.334, "E"))]),
        FishingLocation("473028", "HVOZDNICE 1", "MO OPAVA", 0.0,
                        [(GPSCoordinate(49, 54, 15.754, "N"), GPSCoordinate(17, 53, 54.303, "E")),
                         (GPSCoordinate(49, 56, 41.220, "N"), GPSCoordinate(17, 34, 23.580, "E")),
                         (GPSCoordinate(49, 56, 39.483, "N"), GPSCoordinate(17, 39, 28.013, "E")),
                         (GPSCoordinate(49, 54, 46.735, "N"), GPSCoordinate(17, 39, 9.754, "E")),
                         (GPSCoordinate(49, 54, 50.193, "N"), GPSCoordinate(17, 39, 14.100, "E")),
                         (GPSCoordinate(49, 54, 52.605, "N"), GPSCoordinate(17, 39, 16.919, "E")),
                         (GPSCoordinate(49, 54, 54.893, "N"), GPSCoordinate(17, 39, 15.857, "E"))]),
        FishingLocation("473029", "HUSÍ POTOK 1", "MO FULNEK", 0.0,
                        [(GPSCoordinate(49, 40, 40.155, "N"), GPSCoordinate(18, 0, 35.744, "E")),
                         (GPSCoordinate(49, 47, 54.032, "N"), GPSCoordinate(17, 50, 18.948, "E"))]),
        FishingLocation("473030", "JAVORNICKÝ POTOK", "MO JAVORNÍK", 0.0,
                        [(GPSCoordinate(50, 24, 41.39, "N"), GPSCoordinate(17, 2, 32.567, "E")),
                         (GPSCoordinate(50, 21, 52.534, "N"), GPSCoordinate(16, 55, 19.992, "E"))]),
        FishingLocation("473031", "JIČÍNKA 2", "MO NOVÝ JIČÍN", 0.0,
                        [(GPSCoordinate(49, 36, 46.006, "N"), GPSCoordinate(17, 59, 50.453, "E")),
                         (GPSCoordinate(49, 30, 56.920, "N"), GPSCoordinate(18, 9, 18.537, "E")),
                         (GPSCoordinate(49, 35, 20.620, "N"), GPSCoordinate(18, 1, 20.554, "E")),
                         (GPSCoordinate(49, 31, 36.572, "N"), GPSCoordinate(18, 1, 7.462, "E")),
                         (GPSCoordinate(49, 33, 27.766, "N"), GPSCoordinate(18, 1, 22.243, "E")),
                         (GPSCoordinate(49, 32, 24.003, "N"), GPSCoordinate(17, 58, 17.038, "E"))]),
        FishingLocation("473032", "JUHYNĚ 1", "MO CHORYNĚ", 0.0,
                        [(GPSCoordinate(49, 30, 12.578, "N"), GPSCoordinate(17, 53, 41.555, "E")),
                         (GPSCoordinate(49, 29, 20.198, "N"), GPSCoordinate(17, 53, 3.853, "E"))]),
        FishingLocation("473033", "JUHYNĚ 2", "MO CHORYNĚ", 0.0,
                        [(GPSCoordinate(49, 29, 20.198, "N"), GPSCoordinate(17, 53, 3.853, "E")),
                         (GPSCoordinate(49, 25, 42.227, "N"), GPSCoordinate(17, 47, 14.651, "E"))]),
        FishingLocation("473034", "KLENOS 1", "MO PŘÍBOR", 0.0,
                        [(GPSCoordinate(49, 38, 49.805, "N"), GPSCoordinate(18, 9, 4.138, "E")),
                         (GPSCoordinate(49, 38, 30.259, "N"), GPSCoordinate(18, 11, 32.743, "E"))]),
        FishingLocation("473035", "KOČOVSKÝ POTOK 1", "MO RÝMAŘOV", 0.0,
                        [(GPSCoordinate(49, 55, 29.782, "N"), GPSCoordinate(17, 27, 4.006, "E")),
                         (GPSCoordinate(50, 0, 28.940, "N"), GPSCoordinate(17, 20, 21.781, "E"))]),
        FishingLocation("473036", "KRUPÁ 1", "MO ŠUMPERK", 0.0,
                        [(GPSCoordinate(50, 5, 18.088, "N"), GPSCoordinate(16, 55, 12.823, "E")),
                         (GPSCoordinate(50, 10, 0.802, "N"), GPSCoordinate(16, 56, 36.869, "E"))]),
        FishingLocation("473037", "LAZNICKÝ POTOK 1", "MO LIPNÍK NAD BEČVOU", 0.0,
                        [(GPSCoordinate(49, 31, 5.026, "N"), GPSCoordinate(17, 25, 26.511, "E")),
                         (GPSCoordinate(49, 34, 15.403, "N"), GPSCoordinate(17, 30, 21.452, "E"))]),
        FishingLocation("473038", "LIBINA 1 P", "MO UNIČOV", 0.0,
                        [(GPSCoordinate(49, 53, 39.263, "N"), GPSCoordinate(17, 5, 27.106, "E")),
                         (GPSCoordinate(49, 51, 18.149, "N"), GPSCoordinate(17, 6, 22.638, "E")),
                         (GPSCoordinate(49, 56, 49.148, "N"), GPSCoordinate(17, 4, 56.840, "E"))]),
        FishingLocation("473039", "LOMNÁ 1", "MO JABLUNKOV", 0.0,
                        [(GPSCoordinate(49, 34, 45.391, "N"), GPSCoordinate(18, 45, 50.995, "E")),
                         (GPSCoordinate(49, 29, 55.113, "N"), GPSCoordinate(18, 36, 20.001, "E"))]),
        FishingLocation("473040", "LOSINKA 1", "MO ŠUMPERK", 0.0,
                        [(GPSCoordinate(49, 59, 56.234, "N"), GPSCoordinate(17, 1, 14.106, "E")),
                         (GPSCoordinate(50, 5, 40.078, "N"), GPSCoordinate(17, 3, 39.621, "E"))]),
        FishingLocation("473041", "LUBINA 2 P", "MO PŘÍBOR", 0.0,
                        [(GPSCoordinate(49, 39, 31.869, "N"), GPSCoordinate(18, 8, 31.107, "E")),
                         (GPSCoordinate(49, 37, 22.650, "N"), GPSCoordinate(18, 9, 25.403, "E"))]),
        FishingLocation("473042", "LUBINA 3", "MO FRENŠTÁT POD RADHOŠTĚM", 0.0,
                        [(GPSCoordinate(49, 37, 22.650, "N"), GPSCoordinate(18, 9, 25.403, "E")),
                         (GPSCoordinate(49, 29, 47.790, "N"), GPSCoordinate(18, 11, 41.886, "E")),
                         (GPSCoordinate(49, 35, 25.270, "N"), GPSCoordinate(18, 11, 37.545, "E")),
                         (GPSCoordinate(49, 32, 18.634, "N"), GPSCoordinate(18, 17, 1.271, "E")),
                         (GPSCoordinate(49, 33, 13.546, "N"), GPSCoordinate(18, 12, 5.460, "E")),
                         (GPSCoordinate(49, 30, 25.493, "N"), GPSCoordinate(18, 14, 51.898, "E")),
                         (GPSCoordinate(49, 34, 41.211, "N"), GPSCoordinate(18, 10, 56.718, "E")),
                         (GPSCoordinate(49, 33, 0.041, "N"), GPSCoordinate(18, 9, 36.622, "E")),
                         (GPSCoordinate(49, 32, 27.276, "N"), GPSCoordinate(18, 13, 48.935, "E")),
                         (GPSCoordinate(49, 30, 0.066, "N"), GPSCoordinate(18, 17, 43.592, "E"))]),
        FishingLocation("473043", "LUČINA 1 P", "MO HAVÍŘOV", 0.0,
                        [(GPSCoordinate(49, 47, 11.0, "N"), GPSCoordinate(18, 24, 34.1, "E")),
                         (GPSCoordinate(49, 43, 56.701, "N"), GPSCoordinate(18, 26, 44.974, "E"))]),
        FishingLocation("473044", "LUČINA 3", "MO LUČINA", 0.0,
                        [(GPSCoordinate(49, 42, 10.812, "N"), GPSCoordinate(18, 27, 57.307, "E")),
                         (GPSCoordinate(49, 38, 16.970, "N"), GPSCoordinate(18, 29, 54.566, "E")),
                         (GPSCoordinate(49, 39, 8.251, "N"), GPSCoordinate(18, 27, 25.664, "E"))]),
        FishingLocation("473045", "LUDINA 1", "MO HRANICE NA MORAVĚ", 0.0,
                        [(GPSCoordinate(49, 32, 46.458, "N"), GPSCoordinate(17, 43, 48.886, "E")),
                         (GPSCoordinate(49, 38, 59.822, "N"), GPSCoordinate(17, 42, 34.703, "E"))]),
        FishingLocation("473046", "LUHA 1", "MO NOVÝ JIČÍN", 0.0,
                        [(GPSCoordinate(49, 37, 0.914, "N"), GPSCoordinate(17, 55, 27.292, "E")),
                         (GPSCoordinate(49, 34, 21.102, "N"), GPSCoordinate(17, 52, 26.231, "E"))]),
        FishingLocation("473047", "LUHA 2", "MO HRANICE NA MORAVĚ", 0.0,
                        [(GPSCoordinate(49, 34, 20.661, "N"), GPSCoordinate(17, 52, 25.116, "E")),
                         (GPSCoordinate(49, 40, 3.068, "N"), GPSCoordinate(17, 44, 36.893, "E"))]),
        FishingLocation("473048", "MERTA 1", "MO ŠUMPERK", 0.0,
                        [(GPSCoordinate(50, 0, 12.577, "N"), GPSCoordinate(17, 1, 30.242, "E")),
                         (GPSCoordinate(50, 4, 2.542, "N"), GPSCoordinate(17, 10, 10.975, "E"))]),
        FishingLocation("473049", "MOHELNICE 1", "MO FRÝDEK-MÍSTEK", 0.0,
                        [(GPSCoordinate(49, 36, 58.446, "N"), GPSCoordinate(18, 28, 59.485, "E")),
                         (GPSCoordinate(49, 31, 6.311, "N"), GPSCoordinate(18, 30, 47.250, "E"))]),
        FishingLocation("473050", "MORAVA 23", "MO ŠUMPERK", 0.0,
                        [(GPSCoordinate(49, 56, 31.887, "N"), GPSCoordinate(16, 54, 0.298, "E")),
                         (GPSCoordinate(50, 5, 17.854, "N"), GPSCoordinate(16, 55, 11.960, "E"))]),
        FishingLocation("473051", "MORAVICE 1 P", "MO OPAVA", 0.0,
                        [(GPSCoordinate(49, 54, 22.554, "N"), GPSCoordinate(17, 54, 29.396, "E")),
                         (GPSCoordinate(49, 51, 36.951, "N"), GPSCoordinate(17, 51, 41.962, "E")),
                         (GPSCoordinate(49, 52, 56.578, "N"), GPSCoordinate(17, 52, 48.685, "E")),
                         (GPSCoordinate(49, 51, 36.951, "N"), GPSCoordinate(17, 51, 41.962, "E"))]),
        FishingLocation("473052", "MORAVICE 2", "MO OPAVA", 0.0,
                        [(GPSCoordinate(49, 51, 36.951, "N"), GPSCoordinate(17, 51, 41.962, "E")),
                         (GPSCoordinate(49, 48, 33.292, "N"), GPSCoordinate(17, 47, 57.162, "E")),
                         (GPSCoordinate(49, 51, 37.611, "N"), GPSCoordinate(17, 51, 38.303, "E")),
                         (GPSCoordinate(49, 49, 53.475, "N"), GPSCoordinate(17, 49, 54.108, "E"))]),
        FishingLocation("473053", "MORAVICE 3 P", "MO VÍTKOV", 0.0,
                        [(GPSCoordinate(49, 48, 33.292, "N"), GPSCoordinate(17, 47, 57.162, "E")),
                         (GPSCoordinate(49, 49, 14.080, "N"), GPSCoordinate(17, 42, 58.259, "E"))]),
        FishingLocation("473054", "MORAVICE 4", "MO VÍTKOV", 0.0,
                        [(GPSCoordinate(49, 49, 14.080, "N"), GPSCoordinate(17, 42, 58.259, "E")),
                         (GPSCoordinate(49, 49, 27.52, "N"), GPSCoordinate(17, 40, 00.30, "E"))]),
        FishingLocation("473056", "MORAVICE 7", "MO RÝMAŘOV", 0.0,
                        [(GPSCoordinate(49, 55, 24.240, "N"), GPSCoordinate(17, 27, 4.451, "E")),
                         (GPSCoordinate(49, 56, 7.042, "N"), GPSCoordinate(17, 20, 43.870, "E")),
                         (GPSCoordinate(49, 54, 12.861, "N"), GPSCoordinate(17, 22, 57.278, "E")),
                         (GPSCoordinate(49, 54, 23.861, "N"), GPSCoordinate(17, 23, 4.943, "E"))]),
        FishingLocation("473057", "MORAVICE 8", "MO RÝMAŘOV", 0.0,
                        [(GPSCoordinate(49, 56, 7.042, "N"), GPSCoordinate(17, 20, 43.870, "E")),
                         (GPSCoordinate(50, 3, 26.804, "N"), GPSCoordinate(17, 14, 22.195, "E")),
                         (GPSCoordinate(50, 1, 31.482, "N"), GPSCoordinate(17, 15, 29.318, "E")),
                         (GPSCoordinate(50, 2, 53.603, "N"), GPSCoordinate(17, 13, 30.182, "E")),
                         (GPSCoordinate(50, 1, 33.271, "N"), GPSCoordinate(17, 16, 31.287, "E")),
                         (GPSCoordinate(50, 2, 30.912, "N"), GPSCoordinate(17, 12, 49.320, "E"))]),
        FishingLocation("473058", "MORÁVKA 1", "MO FRÝDEK-MÍSTEK", 0.0,
                        [(GPSCoordinate(49, 40, 19.13, "N"), GPSCoordinate(18, 21, 25.25, "E")),
                         (GPSCoordinate(49, 35, 5.775, "N"), GPSCoordinate(18, 31, 55.431, "E")),
                         (GPSCoordinate(49, 39, 8.251, "N"), GPSCoordinate(18, 27, 25.664, "E"))]),
        FishingLocation("473059", "ODRA 8", "MO VÍTKOV", 0.0,
                        [(GPSCoordinate(49, 40, 27.61, "N"), GPSCoordinate(17, 49, 04.23, "E")),
                         (GPSCoordinate(49, 44, 6.908, "N"), GPSCoordinate(17, 41, 37.913, "E"))]),
        FishingLocation("473060", "OLEŠNÁ 1 P", "MO FRÝDEK-MÍSTEK", 0.0,
                        [(GPSCoordinate(49, 42, 9.454, "N"), GPSCoordinate(18, 18, 7.299, "E")),
                         (GPSCoordinate(49, 39, 57.772, "N"), GPSCoordinate(18, 19, 4.327, "E"))]),
        FishingLocation("473061", "OLEŠNÁ 3", "MO FRÝDEK-MÍSTEK", 0.0,
                        [(GPSCoordinate(49, 39, 13.976, "N"), GPSCoordinate(18, 19, 19.970, "E")),
                         (GPSCoordinate(49, 35, 24.36, "N"), GPSCoordinate(18, 18, 45.28, "E"))]),
        FishingLocation("473062", "OLEŠNICE JESENICKÁ 1", "MO JESENÍK", 0.0,
                        [(GPSCoordinate(50, 18, 14.281, "N"), GPSCoordinate(17, 20, 5.700, "E")),
                         (GPSCoordinate(50, 12, 56.809, "N"), GPSCoordinate(17, 22, 4.766, "E"))]),
        FishingLocation("473063", "OLEŠNICE PŘEROVSKÁ 2", "MO LIPNÍK NAD BEČVOU", 0.0,
                        [(GPSCoordinate(49, 30, 59.689, "N"), GPSCoordinate(17, 25, 21.238, "E")),
                         (GPSCoordinate(49, 36, 20.163, "N"), GPSCoordinate(17, 31, 6.082, "E"))]),
        FishingLocation("473064", "OLŠE 5 P", "MO TŘINEC", 0.0,
                        [(GPSCoordinate(49, 42, 57.657, "N"), GPSCoordinate(18, 37, 43.535, "E")),
                         (GPSCoordinate(49, 38, 27.913, "N"), GPSCoordinate(18, 42, 3.565, "E"))]),
        FishingLocation("473065", "OLŠE 6", "MO BYSTŘICE NAD OLŠÍ", 0.0,
                        [(GPSCoordinate(49, 38, 27.563, "N"), GPSCoordinate(18, 42, 3.527, "E")),
                         (GPSCoordinate(49, 36, 21.011, "N"), GPSCoordinate(18, 44, 28.284, "E"))]),
        FishingLocation("473066", "OLŠE 7", "MO JABLUNKOV", 0.0,
                        [(GPSCoordinate(49, 36, 21.011, "N"), GPSCoordinate(18, 44, 28.284, "E")),
                         (GPSCoordinate(49, 33, 40.734, "N"), GPSCoordinate(18, 50, 39.208, "E")),
                         (GPSCoordinate(49, 34, 50.624, "N"), GPSCoordinate(18, 44, 43.134, "E")),
                         (GPSCoordinate(49, 34, 44.964, "N"), GPSCoordinate(18, 44, 40.817, "E"))]),
        FishingLocation("473067", "ONDŘEJNICE 2", "MO STARÁ VES NAD ODŘEJNICÍ", 0.0,
                        [(GPSCoordinate(49, 43, 46.101, "N"), GPSCoordinate(18, 11, 6.661, "E")),
                         (GPSCoordinate(49, 38, 55.372, "N"), GPSCoordinate(18, 13, 3.045, "E"))]),
        FishingLocation("473068", "OPAVA 7", "MO KRNOV", 0.0,
                        [(GPSCoordinate(50, 5, 45.421, "N"), GPSCoordinate(17, 42, 58.273, "E")),
                         (GPSCoordinate(50, 1, 19.678, "N"), GPSCoordinate(17, 32, 5.955, "E"))]),
        FishingLocation("473069", "OPAVA 8", "MO BRUNTÁL", 0.0,
                        [(GPSCoordinate(50, 1, 19.678, "N"), GPSCoordinate(17, 32, 5.955, "E")),
                         (GPSCoordinate(50, 3, 49.286, "N"), GPSCoordinate(17, 28, 33.902, "E"))]),
        FishingLocation("473070", "OPAVICE (ZLATÁ) 1", "MO KRNOV", 0.0,
                        [(GPSCoordinate(50, 5, 45.854, "N"), GPSCoordinate(17, 42, 58.229, "E")),
                         (GPSCoordinate(50, 9, 45.618, "N"), GPSCoordinate(17, 34, 50.927, "E"))]),
        FishingLocation("473071", "OPAVICE (ZLATÁ) 2", "MO KRNOV", 0.0,
                        [(GPSCoordinate(50, 9, 45.723, "N"), GPSCoordinate(17, 34, 50.642, "E")),
                         (GPSCoordinate(50, 12, 34.996, "N"), GPSCoordinate(17, 23, 6.982, "E"))]),
        FishingLocation("473072", "OSKAVA 4", "MO UNIČOV", 0.0,
                        [(GPSCoordinate(49, 48, 38.042, "N"), GPSCoordinate(17, 7, 14.799, "E")),
                         (GPSCoordinate(49, 55, 14.460, "N"), GPSCoordinate(17, 8, 56.616, "E"))]),
        FishingLocation("473073", "OSLAVA ŠTERNBERSKÁ 1", "MO ŠTERNBERK", 0.0,
                        [(GPSCoordinate(49, 47, 43.995, "N"), GPSCoordinate(17, 7, 41.343, "E")),
                         (GPSCoordinate(49, 54, 58.609, "N"), GPSCoordinate(17, 17, 15.506, "E"))]),
        FishingLocation("473074", "OSOBLAHA 2", "MO KRNOV", 0.0,
                        [(GPSCoordinate(50, 14, 7.538, "N"), GPSCoordinate(17, 41, 3.362, "E")),
                         (GPSCoordinate(50, 12, 40.710, "N"), GPSCoordinate(17, 25, 22.043, "E"))]),
        FishingLocation("473075", "OSTRAVICE 3", "MO FRÝDEK-MÍSTEK", 0.0,
                        [(GPSCoordinate(49, 41, 16.745, "N"), GPSCoordinate(18, 19, 57.600, "E")),
                         (GPSCoordinate(49, 36, 27.136, "N"), GPSCoordinate(18, 21, 32.429, "E"))]),
        FishingLocation("473076", "OSTRAVICE 4", "MO FRÝDLANT NAD OSTRAVICÍ", 0.0,
                        [(GPSCoordinate(49, 36, 27.136, "N"), GPSCoordinate(18, 21, 32.429, "E")),
                         (GPSCoordinate(49, 30, 44.755, "N"), GPSCoordinate(18, 24, 56.071, "E")),
                         (GPSCoordinate(49, 34, 26.006, "N"), GPSCoordinate(18, 21, 53.738, "E")),
                         (GPSCoordinate(49, 34, 18.452, "N"), GPSCoordinate(18, 22, 7.145, "E"))]),
        FishingLocation("473077", "OSTRAVICE 6", "MO FRÝDLANT NAD OSTRAVICÍ", 0.0,
                        [(GPSCoordinate(49, 27, 40.517, "N"), GPSCoordinate(18, 27, 5.243, "E")),
                         (GPSCoordinate(49, 24, 44.621, "N"), GPSCoordinate(18, 22, 16.995, "E")),
                         (GPSCoordinate(49, 29, 54.063, "N"), GPSCoordinate(18, 32, 34.906, "E")),
                         (GPSCoordinate(49, 28, 24.812, "N"), GPSCoordinate(18, 25, 37.766, "E")),
                         (GPSCoordinate(49, 28, 28.926, "N"), GPSCoordinate(18, 23, 28.666, "E")),
                         (GPSCoordinate(49, 27, 17.936, "N"), GPSCoordinate(18, 28, 3.808, "E")),
                         (GPSCoordinate(49, 27, 17.154, "N"), GPSCoordinate(18, 28, 8.052, "E"))]),
        FishingLocation("473078", "PODOLSKÝ POTOK 1", "MO RÝMAŘOV", 0.0,
                        [(GPSCoordinate(49, 56, 7.017, "N"), GPSCoordinate(17, 20, 43.639, "E")),
                         (GPSCoordinate(49, 57, 5.024, "N"), GPSCoordinate(17, 14, 41.208, "E"))]),
        FishingLocation("473079", "POLICKÝ POTOK", "MO MOHELNICE", 0.0,
                        [(GPSCoordinate(49, 47, 20.954, "N"), GPSCoordinate(16, 57, 50.706, "E")),
                         (GPSCoordinate(49, 52, 49.831, "N"), GPSCoordinate(17, 2, 12.083, "E"))]),
        FishingLocation("473080", "RAČÍ POTOK", "MO JAVORNÍK", 0.0,
                        [(GPSCoordinate(50, 24, 24.909, "N"), GPSCoordinate(17, 3, 11.497, "E")),
                         (GPSCoordinate(50, 18, 50.702, "N"), GPSCoordinate(16, 57, 28.484, "E")),
                         (GPSCoordinate(50, 24, 19.790, "N"), GPSCoordinate(17, 5, 0.524, "E")),
                         (GPSCoordinate(50, 18, 53.622, "N"), GPSCoordinate(16, 58, 21.279, "E"))]),
        FishingLocation("473081", "ROKYTENKA 1", "MO VSETÍN", 0.0,
                        [(GPSCoordinate(49, 20, 28.510, "N"), GPSCoordinate(17, 59, 23.181, "E")),
                         (GPSCoordinate(49, 19, 2.294, "N"), GPSCoordinate(17, 54, 4.457, "E"))]),
        FishingLocation("473082", "ROPIČANKA 1", "MO ČESKÝ TĚŠÍN", 0.0,
                        [(GPSCoordinate(49, 43, 42.589, "N"), GPSCoordinate(18, 37, 35.460, "E")),
                         (GPSCoordinate(49, 35, 56.850, "N"), GPSCoordinate(18, 35, 23.152, "E"))]),
        FishingLocation("473083", "SÁZAVA MORAVSKÁ 2 P", "MO ZÁBŘEH NA MORAVĚ", 0.0,
                        [(GPSCoordinate(49, 52, 4.316, "N"), GPSCoordinate(16, 50, 43.205, "E")),
                         (GPSCoordinate(49, 51, 55.692, "N"), GPSCoordinate(16, 44, 47.557, "E"))]),
        FishingLocation("473084", "SEDLNIČKA 1", "MO PŘÍBOR", 0.0,
                        [(GPSCoordinate(49, 42, 1.719, "N"), GPSCoordinate(18, 4, 0.194, "E")),
                         (GPSCoordinate(49, 32, 44.237, "N"), GPSCoordinate(18, 7, 51.907, "E"))]),
        FishingLocation("473085", "SENICE 1", "MO VSETÍN", 0.0,
                        [(GPSCoordinate(49, 18, 44.876, "N"), GPSCoordinate(18, 0, 5.286, "E")),
                         (GPSCoordinate(49, 15, 37.908, "N"), GPSCoordinate(18, 9, 25.074, "E"))]),
        FishingLocation("473086", "SETINA 1", "MO BÍLOVEC", 0.0,
                        [(GPSCoordinate(49, 44, 31.702, "N"), GPSCoordinate(18, 5, 27.181, "E")),
                         (GPSCoordinate(49, 49, 36.647, "N"), GPSCoordinate(17, 54, 55.159, "E")),
                         (GPSCoordinate(49, 45, 42.3, "N"), GPSCoordinate(18, 2, 11.1, "E")),
                         (GPSCoordinate(49, 44, 37.030, "N"), GPSCoordinate(18, 5, 18.145, "E"))]),
        FishingLocation("473087", "SITKA 2", "MO ŠTERNBERK", 0.0,
                        [(GPSCoordinate(49, 43, 16.753, "N"), GPSCoordinate(17, 16, 47.264, "E")),
                         (GPSCoordinate(49, 52, 57.362, "N"), GPSCoordinate(17, 18, 57.388, "E")),
                         (GPSCoordinate(49, 47, 5.397, "N"), GPSCoordinate(17, 11, 40.259, "E")),
                         (GPSCoordinate(49, 52, 8.054, "N"), GPSCoordinate(17, 17, 28.086, "E"))]),
        FishingLocation("473088", "SKOROŠICKÝ POTOK 1", "MO JAVORNÍK", 0.0,
                        [(GPSCoordinate(50, 20, 17.541, "N"), GPSCoordinate(17, 7, 4.594, "E")),
                         (GPSCoordinate(50, 16, 57.574, "N"), GPSCoordinate(17, 1, 21.028, "E"))]),
        FishingLocation("473089", "STAŘÍČ 1", "MO JESENÍK", 0.0,
                        [(GPSCoordinate(50, 14, 10.113, "N"), GPSCoordinate(17, 12, 12.955, "E")),
                         (GPSCoordinate(50, 13, 54.720, "N"), GPSCoordinate(17, 2, 30.641, "E"))]),
        FishingLocation("473090", "STONÁVKA 1 P", "MO KARVINÁ", 0.0,
                        [(GPSCoordinate(49, 49, 45.787, "N"), GPSCoordinate(18, 31, 18.959, "E")),
                         (GPSCoordinate(49, 46, 26.683, "N"), GPSCoordinate(18, 31, 3.230, "E"))]),
        FishingLocation("473091", "STONÁVKA 3", "MO ČESKÝ TĚŠÍN", 0.0,
                        [(GPSCoordinate(49, 43, 44.016, "N"), GPSCoordinate(18, 29, 58.723, "E")),
                         (GPSCoordinate(49, 37, 32.884, "N"), GPSCoordinate(18, 31, 3.000, "E")),
                         (GPSCoordinate(49, 39, 40.238, "N"), GPSCoordinate(18, 31, 30.315, "E")),
                         (GPSCoordinate(49, 38, 32.067, "N"), GPSCoordinate(18, 32, 14.080, "E"))]),
        FishingLocation("473092", "ŠUMICE 1 P", "MO OLOMOUC", 0.0,
                        [(GPSCoordinate(49, 36, 8.065, "N"), GPSCoordinate(17, 3, 53.521, "E")),
                         (GPSCoordinate(49, 38, 59.958, "N"), GPSCoordinate(16, 57, 51.264, "E"))]),
        FishingLocation("473093", "TRNÁVKA 1", "MO STARÁ VES NAD ONDŘEJNICÍ", 0.0,
                        [(GPSCoordinate(49, 43, 26.215, "N"), GPSCoordinate(18, 10, 0.787, "E")),
                         (GPSCoordinate(49, 39, 17.939, "N"), GPSCoordinate(18, 11, 35.275, "E"))]),
        FishingLocation("473094", "TRUSOVICKÝ POTOK 1", "MO DOMAŠOV NAD BYSTŘICÍ", 0.0,
                        [(GPSCoordinate(49, 39, 25.460, "N"), GPSCoordinate(17, 17, 13.881, "E")),
                         (GPSCoordinate(49, 48, 46.576, "N"), GPSCoordinate(17, 21, 15.492, "E")),
                         (GPSCoordinate(49, 46, 37.162, "N"), GPSCoordinate(17, 20, 40.233, "E"))]),
        FishingLocation("473095", "TYRA 1", "MO TŘINEC", 0.0,
                        [(GPSCoordinate(49, 40, 59.071, "N"), GPSCoordinate(18, 39, 22.678, "E")),
                         (GPSCoordinate(49, 34, 45.678, "N"), GPSCoordinate(18, 37, 48.312, "E")),
                         (GPSCoordinate(49, 37, 24.249, "N"), GPSCoordinate(18, 38, 59.316, "E"))]),
        FishingLocation("473096", "VELIČKA 1", "MO HRANICE", 0.0,
                        [(GPSCoordinate(49, 32, 46.250, "N"), GPSCoordinate(17, 43, 48.011, "E")),
                         (GPSCoordinate(49, 38, 20.866, "N"), GPSCoordinate(17, 36, 8.051, "E"))]),
        FishingLocation("473097", "VIDNÁVKA 1", "MO JAVORNÍK", 0.0,
                        [(GPSCoordinate(50, 23, 20.313, "N"), GPSCoordinate(17, 11, 27.786, "E")),
                         (GPSCoordinate(50, 15, 28.692, "N"), GPSCoordinate(17, 9, 34.236, "E"))]),
        FishingLocation("473098", "OPAVA 9", "MO VRBNO POD PRADĚDEM", 0.0,
                        [(GPSCoordinate(49, 33, 38.553, "N"), GPSCoordinate(18, 33, 0.312, "E")),
                         (GPSCoordinate(49, 30, 3.599, "N"), GPSCoordinate(18, 32, 37.418, "E"))]),
        FishingLocation("473099", "PRUDNÍK 2 P", "MO ZLATÉ HORY", 0.0,
                        [(GPSCoordinate(50, 16, 44.709, "N"), GPSCoordinate(17, 24, 4.947, "E")),
                         (GPSCoordinate(50, 12, 26.478, "N"), GPSCoordinate(17, 24, 38.781, "E")),
                         (GPSCoordinate(50, 15, 27.880, "N"), GPSCoordinate(17, 23, 57.956, "E"))]),
        FishingLocation("473101", "STŘÍBRNÝ POTOK 1", "MO JAVORNÍK", 0.0,
                        [(GPSCoordinate(49, 46, 58.755, "N"), GPSCoordinate(16, 57, 21.365, "E")),
                         (GPSCoordinate(49, 48, 23.379, "N"), GPSCoordinate(16, 47, 49.626, "E")),
                         (GPSCoordinate(49, 47, 2.277, "N"), GPSCoordinate(16, 46, 35.604, "E"))]),
        FishingLocation("473102", "MÍROVKA 1", "MO MOHELNICE", 0.0,
                        [(GPSCoordinate(50, 3, 49.503, "N"), GPSCoordinate(17, 28, 34.375, "E")),
                         (GPSCoordinate(50, 7, 29.580, "N"), GPSCoordinate(17, 22, 3.303, "E"))]),
        FishingLocation("473104", "OSTRAVICE 2", "MO ČRS OSTRAVA", 0.0,
                        [(GPSCoordinate(49, 48, 9.692, "N"), GPSCoordinate(18, 16, 56.964, "E")),
                         (GPSCoordinate(49, 41, 16.745, "N"), GPSCoordinate(18, 19, 57.600, "E")),
                         (GPSCoordinate(49, 48, 9.692, "N"), GPSCoordinate(18, 16, 56.964, "E")),
                         (GPSCoordinate(49, 45, 29.555, "N"), GPSCoordinate(18, 18, 18.383, "E"))]),
        FishingLocation("473105", "MOŠTĚNKA 2", "MO ČRS PŘEROV", 0.0,
                        [(GPSCoordinate(49, 25, 33.773, "N"), GPSCoordinate(17, 30, 13.378, "E")),
                         (GPSCoordinate(49, 25, 31.666, "N"), GPSCoordinate(17, 32, 51.504, "E")),
                         (GPSCoordinate(49, 25, 29.643, "N"), GPSCoordinate(17, 32, 40.282, "E")),
                         (GPSCoordinate(49, 22, 58.248, "N"), GPSCoordinate(17, 40, 32.452, "E"))]),
        FishingLocation("473106", "OPAVA 9 P", "MO VRBNO POD PRADĚDEM", 0.0,
                        [(GPSCoordinate(50, 7, 1.825, "N"), GPSCoordinate(17, 23, 32.886, "E"))]),
        FishingLocation("473108", "JIČÍNKA 1P", "MO NOVÝ JIČÍN", 0.0,
                        [(GPSCoordinate(49, 39, 57.088, "N"), GPSCoordinate(17, 59, 32.753, "E")),
                         (GPSCoordinate(49, 36, 46.006, "N"), GPSCoordinate(17, 59, 50.453, "E"))]),
        FishingLocation("473300", "BEČVA ROŽNOVSKÁ 1", "MO VALAŠSKÉ MEZIŘÍČÍ   CH A P", 0.0,
                        [(GPSCoordinate(49, 28, 11.392, "N"), GPSCoordinate(17, 57, 16.836, "E")),
                         (GPSCoordinate(49, 28, 26.990, "N"), GPSCoordinate(17, 59, 36.268, "E"))]),
        FishingLocation("473301", "ČERNÝ POTOK 1", "MO BRUNTÁL", 0.0,
                        [(GPSCoordinate(49, 57, 21.797, "N"), GPSCoordinate(17, 29, 25.425, "E")),
                         (GPSCoordinate(50, 2, 7.155, "N"), GPSCoordinate(17, 19, 25.011, "E")),
                         (GPSCoordinate(49, 58, 43.224, "N"), GPSCoordinate(17, 28, 1.967, "E")),
                         (GPSCoordinate(49, 59, 36.794, "N"), GPSCoordinate(17, 27, 48.692, "E"))]),
        FishingLocation("473500", "STŘEDNÍ OPAVA 1", "MO VRBNO P. PRADĚDEM", 0.0,
                        [(GPSCoordinate(50, 7, 29.580, "N"), GPSCoordinate(17, 22, 3.303, "E")),
                         (GPSCoordinate(50, 6, 17.398, "N"), GPSCoordinate(17, 16, 11.203, "E"))]),
    ]
