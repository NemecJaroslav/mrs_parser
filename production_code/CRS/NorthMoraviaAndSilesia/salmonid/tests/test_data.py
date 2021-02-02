from production_code.common.fishing_location import FishingLocation
from production_code.common.parser import GPSCoordinate


def get_expected_fishing_locations():
    return [
        FishingLocation("473001", "BEČVA ROŽNOVSKÁ 1", "MO VALAŠSKÉ MEZIŘÍČÍ", 0.0,
                        [(GPSCoordinate(49, 28, 23.571, "N"), GPSCoordinate(17, 58, 24.85, "E")),
                         (GPSCoordinate(49, 27, 50.285, "N"), GPSCoordinate(18, 3, 14.505, "E"))]),
        FishingLocation("473002", "BEČVA ROŽNOVSKÁ 2", "MO ROŽNOV POD RADHOŠTĚM", 0.0,
                        [(GPSCoordinate(49, 27, 50.284, "N"), GPSCoordinate(18, 3, 14.53, "E")),
                         (GPSCoordinate(49, 25, 21.042, "N"), GPSCoordinate(18, 18, 50.902, "E")),
                         (GPSCoordinate(49, 25, 24.142, "N"), GPSCoordinate(18, 19, 5.337, "E"))]),
        FishingLocation("473003", "BEČVA VSETÍNSKÁ 1", "MO VALAŠSKÉ MEZIŘÍČÍ", 0.0,
                        [(GPSCoordinate(49, 28, 12.059, "N"), GPSCoordinate(17, 57, 15.966, "E")),
                         (GPSCoordinate(49, 25, 9.233, "N"), GPSCoordinate(17, 57, 35.957, "E"))]),
        FishingLocation("473004", "BEČVA VSETÍNSKÁ 2", "MO VSETÍN", 0.0,
                        [(GPSCoordinate(49, 25, 9.391, "N"), GPSCoordinate(17, 57, 34.849, "E")),
                         (GPSCoordinate(49, 19, 29.199, "N"), GPSCoordinate(17, 59, 48.483, "E"))]),
        FishingLocation("473005", "BEČVA VSETÍNSKÁ 3", "MO VSETÍN", 0.0,
                        [(GPSCoordinate(49, 19, 28.692, "N"), GPSCoordinate(17, 59, 48.081, "E")),
                         (GPSCoordinate(49, 19, 32.139, "N"), GPSCoordinate(18, 9, 46.821, "E"))]),
        FishingLocation("473006", "BEČVA VSETÍNSKÁ 4 P", "MO VSETÍN", 0.0,
                        [(GPSCoordinate(49, 19, 32.134, "N"), GPSCoordinate(18, 9, 47.019, "E")),
                         (GPSCoordinate(49, 23, 51.182, "N"), GPSCoordinate(18, 23, 51.103, "E"))]),
        FishingLocation("473007", "BĚLÁ JESENICKÁ 1", "MO JESENÍK", 0.0,
                        [(GPSCoordinate(50, 18, 23.981, "N"), GPSCoordinate(17, 21, 11.436, "E")),
                         (GPSCoordinate(50, 15, 15.521, "N"), GPSCoordinate(17, 13, 32.006, "E"))]),
        FishingLocation("473008", "BĚLÁ JESENICKÁ 2", "MO JESENÍK", 0.0,
                        [(GPSCoordinate(50, 14, 9.889, "N"), GPSCoordinate(17, 12, 13.597, "E")),
                         (GPSCoordinate(50, 7, 8.223, "N"), GPSCoordinate(17, 14, 8.987, "E"))]),
        FishingLocation("473009", "BÍLOVKA 1", "MO BÍLOVEC", 0.0,
                        [(GPSCoordinate(49, 43, 34.6, "N"), GPSCoordinate(18, 8, 2.034, "E")),
                         (GPSCoordinate(49, 43, 47.495, "N"), GPSCoordinate(18, 8, 22.678, "E")),
                         (GPSCoordinate(49, 45, 45.290, "N"), GPSCoordinate(17, 59, 31.794, "E"))]),
        FishingLocation("473010", "BRANNÁ 1", "MO ŠUMPERK", 0.0,
                        [(GPSCoordinate(50, 4, 35.656, "N"), GPSCoordinate(16, 56, 4.023, "E")),
                         (GPSCoordinate(50, 8, 53.277, "N"), GPSCoordinate(17, 0, 48.952, "E"))]),
        FishingLocation("473011", "BŘEZNÁ 1", "MO ZÁBŘEH NA MORAVĚ", 0.0,
                        [(GPSCoordinate(49, 52, 26.988, "N"), GPSCoordinate(16, 46, 9.840, "E")),
                         (GPSCoordinate(49, 57, 18.261, "N"), GPSCoordinate(16, 46, 1.338, "E"))]),
        FishingLocation("473012", "BŘEZNÁ 2", "MO ZÁBŘEH NA MORAVĚ", 0.0,
                        [(GPSCoordinate(49, 57, 18.634, "N"), GPSCoordinate(16, 46, 1.326, "E")),
                         (GPSCoordinate(50, 1, 10.706, "N"), GPSCoordinate(16, 44, 43.571, "E"))]),
        FishingLocation("473013", "BUDIŠOVKA 1 P", "MO VÍTKOV", 0.0,
                        [(GPSCoordinate(49, 44, 6.663, "N"), GPSCoordinate(17, 41, 37.734, "E")),
                         (GPSCoordinate(49, 48, 3.918, "N"), GPSCoordinate(17, 35, 34.638, "E"))]),
        FishingLocation("473014", "BYSTŘICE HANÁCKÁ 2 P", "MO VELKÁ BYSTŘICE", 0.0,
                        [(GPSCoordinate(49, 35, 38.146, "N"), GPSCoordinate(17, 19, 52.912, "E")),
                         (GPSCoordinate(49, 39, 15.305, "N"), GPSCoordinate(17, 24, 38.151, "E"))]),
        FishingLocation("473015", "BYSTŘICE HANÁCKÁ 3", "MO DOMAŠOV NAD BYSTŘICÍ", 0.0,
                        [(GPSCoordinate(49, 39, 15.305, "N"), GPSCoordinate(17, 24, 38.151, "E")),
                         (GPSCoordinate(49, 44, 33.129, "N"), GPSCoordinate(17, 26, 46.811, "E")),
                         (GPSCoordinate(49, 44, 54.742, "N"), GPSCoordinate(17, 27, 21.01, "E"))]),
        FishingLocation("473016", "BYSTŘICE HANÁCKÁ 4", "MO DOMAŠOV NAD BYSTŘICÍ", 0.0,
                        [(GPSCoordinate(49, 44, 33.162, "N"), GPSCoordinate(17, 26, 46.763, "E")),
                         (GPSCoordinate(49, 50, 2.747, "N"), GPSCoordinate(17, 24, 2.368, "E")),
                         (GPSCoordinate(49, 46, 50.737, "N"), GPSCoordinate(17, 26, 29.686, "E")),
                         (GPSCoordinate(49, 47, 51.145, "N"), GPSCoordinate(17, 26, 44.507, "E"))]),
        FishingLocation("473017", "BYSTŘICE VALAŠSKÁ 1 P", "MO VSETÍN", 0.0,
                        [(GPSCoordinate(49, 25, 12.295, "N"), GPSCoordinate(17, 57, 51.085, "E")),
                         (GPSCoordinate(49, 23, 41.621, "N"), GPSCoordinate(18, 9, 45.035, "E"))]),
        FishingLocation("473018", "ČELADENKA 1", "MO FRÝDLANT NAD OSTRAVICÍ", 0.0,
                        [(GPSCoordinate(49, 34, 7.52, "N"), GPSCoordinate(18, 21, 45.99, "E")),
                         (GPSCoordinate(49, 27, 11.437, "N"), GPSCoordinate(18, 22, 13.214, "E")),
                         (GPSCoordinate(49, 34, 3.787, "N"), GPSCoordinate(18, 21, 17.844, "E")),
                         (GPSCoordinate(49, 34, 4.612, "N"), GPSCoordinate(18, 21, 31.82, "E"))]),
        FishingLocation("473019", "ČERNÁ OPAVA 1", "MO VRBNO POD PRADĚDEM", 0.0,
                        [(GPSCoordinate(50, 7, 32.177, "N"), GPSCoordinate(17, 22, 47.336, "E")),
                         (GPSCoordinate(50, 10, 49.228, "N"), GPSCoordinate(17, 17, 12.07, "E"))]),
        FishingLocation("473021", "ČERVENÝ POTOK 1", "MO JAVORNÍK", 0.0,
                        [(GPSCoordinate(50, 21, 46.532, "N"), GPSCoordinate(17, 9, 53.885, "E")),
                         (GPSCoordinate(50, 17, 46.251, "N"), GPSCoordinate(17, 10, 32.787, "E")),
                         (GPSCoordinate(50, 20, 41.15, "N"), GPSCoordinate(17, 10, 34.049, "E")),
                         (GPSCoordinate(50, 19, 4.662, "N"), GPSCoordinate(17, 10, 1.573, "E"))]),
        FishingLocation("473022", "HOŘINA 1", "MO KRNOV", 0.0,
                        [(GPSCoordinate(50, 1, 10.166, "N"), GPSCoordinate(17, 46, 23.63, "E")),
                         (GPSCoordinate(49, 58, 51.197, "N"), GPSCoordinate(17, 39, 0.735, "E"))]),
        FishingLocation("473023", "DESNÁ 2", "MO ŠUMPERK", 0.0,
                        [(GPSCoordinate(49, 57, 11.642, "N"), GPSCoordinate(16, 59, 25.638, "E")),
                         (GPSCoordinate(50, 4, 9.264, "N"), GPSCoordinate(17, 5, 13.452, "E"))]),
        FishingLocation("473024", "DESNÁ 3", "MO ŠUMPERK", 0.0,
                        [(GPSCoordinate(50, 4, 9.265, "N"), GPSCoordinate(17, 5, 13.427, "E")),
                         (GPSCoordinate(50, 5, 56.594, "N"), GPSCoordinate(17, 6, 26.027, "E")),
                         (GPSCoordinate(50, 5, 56.626, "N"), GPSCoordinate(17, 6, 26.054, "E")),
                         (GPSCoordinate(50, 9, 5.852, "N"), GPSCoordinate(17, 7, 21.012, "E")),
                         (GPSCoordinate(50, 5, 56.594, "N"), GPSCoordinate(17, 6, 26.027, "E")),
                         (GPSCoordinate(50, 5, 17.404, "N"), GPSCoordinate(17, 10, 49.374, "E"))]),
        FishingLocation("473025", "HERLIČKA 1", "MO OPAVA", 0.0,
                        [(GPSCoordinate(49, 59, 33.806, "N"), GPSCoordinate(17, 49, 17.372, "E")),
                         (GPSCoordinate(49, 58, 6.23, "N"), GPSCoordinate(17, 43, 54.446, "E"))]),
        FishingLocation("473026", "HLUCHOVÁ 1", "MO BYSTŘICE NAD OLŠÍ", 0.0,
                        [(GPSCoordinate(49, 37, 53.166, "N"), GPSCoordinate(18, 43, 0.341, "E")),
                         (GPSCoordinate(49, 39, 20.937, "N"), GPSCoordinate(18, 45, 31.453, "E"))]),
        FishingLocation("473027", "HROZOVÁ 1", "MO KRNOV", 0.0,
                        [(GPSCoordinate(50, 14, 41.992, "N"), GPSCoordinate(17, 43, 5.318, "E")),
                         (GPSCoordinate(50, 10, 45.482, "N"), GPSCoordinate(17, 36, 26.9, "E"))]),
        FishingLocation("473028", "HVOZDNICE 1", "MO OPAVA", 0.0,
                        [(GPSCoordinate(49, 54, 15.574, "N"), GPSCoordinate(17, 53, 53.376, "E")),
                         (GPSCoordinate(49, 55, 0.676, "N"), GPSCoordinate(17, 41, 29.259, "E")),
                         (GPSCoordinate(49, 56, 46.803, "N"), GPSCoordinate(17, 39, 30.639, "E"))]),
        FishingLocation("473029", "HUSÍ POTOK 1", "MO FULNEK", 0.0,
                        [(GPSCoordinate(49, 40, 40.018, "N"), GPSCoordinate(18, 0, 35.324, "E")),
                         (GPSCoordinate(49, 45, 20.627, "N"), GPSCoordinate(17, 49, 16.184, "E"))]),
        FishingLocation("473030", "JAVORNICKÝ POTOK", "MO JAVORNÍK", 0.0,
                        [(GPSCoordinate(50, 24, 41.39, "N"), GPSCoordinate(17, 2, 32.567, "E")),
                         (GPSCoordinate(50, 22, 21.666, "N"), GPSCoordinate(16, 55, 55.825, "E"))]),
        FishingLocation("473031", "JIČÍNKA 2", "MO NOVÝ JIČÍN", 0.0,
                        [(GPSCoordinate(49, 37, 34.888, "N"), GPSCoordinate(17, 59, 29.21, "E")),
                         (GPSCoordinate(49, 31, 11.382, "N"), GPSCoordinate(18, 8, 27.675, "E")),
                         (GPSCoordinate(49, 35, 20.764, "N"), GPSCoordinate(18, 1, 20.94, "E")),
                         (GPSCoordinate(49, 31, 37.149, "N"), GPSCoordinate(18, 1, 10.668, "E")),
                         (GPSCoordinate(49, 33, 27.951, "N"), GPSCoordinate(18, 1, 22.359, "E")),
                         (GPSCoordinate(49, 32, 43.52, "N"), GPSCoordinate(17, 58, 19.751, "E"))]),
        FishingLocation("473032", "JUHYNĚ 1", "MO CHORYNĚ", 0.0,
                        [(GPSCoordinate(49, 30, 12.252, "N"), GPSCoordinate(17, 53, 42.173, "E")),
                         (GPSCoordinate(49, 29, 30.503, "N"), GPSCoordinate(17, 53, 23.45, "E"))]),
        FishingLocation("473033", "JUHYNĚ 2", "MO KELČ", 0.0,
                        [(GPSCoordinate(49, 29, 30.503, "N"), GPSCoordinate(17, 53, 23.45, "E")),
                         (GPSCoordinate(49, 25, 42.254, "N"), GPSCoordinate(17, 47, 14.74, "E"))]),
        FishingLocation("473034", "KLENOS 1", "MO PŘÍBOR", 0.0, []),
        FishingLocation("473035", "KOČOVSKÝ POTOK 1", "MO RÝMAŘOV", 0.0,
                        [(GPSCoordinate(49, 55, 29.62, "N"), GPSCoordinate(17, 27, 7.82, "E")),
                         (GPSCoordinate(49, 58, 47.708, "N"), GPSCoordinate(17, 22, 27.173, "E"))]),
        FishingLocation("473036", "KRUPÁ 1", "MO ŠUMPERK", 0.0,
                        [(GPSCoordinate(50, 5, 18.23, "N"), GPSCoordinate(16, 55, 11.809, "E")),
                         (GPSCoordinate(50, 10, 4.259, "N"), GPSCoordinate(16, 56, 36.087, "E"))]),
        FishingLocation("473037", "LAZNICKÝ POTOK 1", "MO LIPNÍK NAD BEČVOU", 0.0, []),
        FishingLocation("473038", "LIBINA 1 P", "MO UNIČOV", 0.0,
                        [(GPSCoordinate(49, 52, 53.96, "N"), GPSCoordinate(17, 5, 7.215, "E"))]),
        FishingLocation("473039", "LOMNÁ 1", "MO JABLUNKOV", 0.0,
                        [(GPSCoordinate(49, 34, 45.391, "N"), GPSCoordinate(18, 45, 50.995, "E")),
                         (GPSCoordinate(49, 31, 19.39, "N"), GPSCoordinate(18, 37, 55.943, "E"))]),
        FishingLocation("473040", "LOSINKA 1", "MO ŠUMPERK", 0.0, []),
        FishingLocation("473041", "LUBINA 2 P", "MO PŘÍBOR", 0.0,
                        [(GPSCoordinate(49, 39, 31.9, "N"), GPSCoordinate(18, 8, 31.252, "E")),
                         (GPSCoordinate(49, 37, 2.425, "N"), GPSCoordinate(18, 10, 10.452, "E"))]),
        FishingLocation("473042", "LUBINA 3", "MO FRENŠTÁT POD RADHOŠTĚM", 0.0,
                        [(GPSCoordinate(49, 37, 2.407, "N"), GPSCoordinate(18, 10, 10.526, "E")),
                         (GPSCoordinate(49, 30, 35.798, "N"), GPSCoordinate(18, 11, 53.956, "E")),
                         (GPSCoordinate(49, 35, 24.898, "N"), GPSCoordinate(18, 11, 37.716, "E")),
                         (GPSCoordinate(49, 32, 18.12, "N"), GPSCoordinate(18, 16, 59.359, "E")),
                         (GPSCoordinate(49, 33, 14.135, "N"), GPSCoordinate(18, 12, 5.547, "E")),
                         (GPSCoordinate(49, 30, 27.738, "N"), GPSCoordinate(18, 14, 49.754, "E")),
                         (GPSCoordinate(49, 34, 41.261, "N"), GPSCoordinate(18, 10, 57.191, "E")),
                         (GPSCoordinate(49, 33, 0.013, "N"), GPSCoordinate(18, 171, 1.240, "E")),
                         (GPSCoordinate(49, 32, 27.301, "N"), GPSCoordinate(18, 13, 48.549, "E")),
                         (GPSCoordinate(49, 31, 29.155, "N"), GPSCoordinate(18, 15, 52.761, "E"))]),
        FishingLocation("473043", "LUČINA 1 P", "MO HAVÍŘOV", 0.0,
                        [(GPSCoordinate(49, 46, 8.553, "N"), GPSCoordinate(18, 26, 0.987, "E")),
                         (GPSCoordinate(49, 43, 56.545, "N"), GPSCoordinate(18, 26, 45.254, "E"))]),
        FishingLocation("473044", "LUČINA 3", "MO LUČINA", 0.0,
                        [(GPSCoordinate(49, 41, 40.698, "N"), GPSCoordinate(18, 27, 44.515, "E")),
                         (GPSCoordinate(49, 39, 2.301, "N"), GPSCoordinate(18, 27, 6.398, "E"))]),
        FishingLocation("473045", "LUDINA 1", "MO HRANICE NA MORAVĚ", 0.0,
                        [(GPSCoordinate(49, 32, 46.289, "N"), GPSCoordinate(17, 43, 48.307, "E")),
                         (GPSCoordinate(49, 37, 58.181, "N"), GPSCoordinate(17, 43, 57.59, "E"))]),
        FishingLocation("473046", "LUHA 1", "MO NOVÝ JIČÍN", 0.0,
                        [(GPSCoordinate(49, 37, 1.241, "N"), GPSCoordinate(17, 55, 29.074, "E")),
                         (GPSCoordinate(49, 34, 21.102, "N"), GPSCoordinate(17, 52, 26.231, "E"))]),
        FishingLocation("473047", "LUHA 2", "MO HRANICE NA MORAVĚ", 0.0,
                        [(GPSCoordinate(49, 34, 20.771, "N"), GPSCoordinate(17, 52, 25.241, "E")),
                         (GPSCoordinate(49, 39, 58.581, "N"), GPSCoordinate(17, 44, 28.936, "E"))]),
        FishingLocation("473048", "MERTA 1", "MO ŠUMPERK", 0.0,
                        [(GPSCoordinate(50, 0, 12.195, "N"), GPSCoordinate(17, 1, 29.653, "E")),
                         (GPSCoordinate(50, 1, 53.042, "N"), GPSCoordinate(17, 7, 40.921, "E"))]),
        FishingLocation("473049", "MOHELNICE 1", "MO FRÝDEK-MÍSTEK", 0.0, []),
        FishingLocation("473050", "MORAVA 23", "MO ŠUMPERK", 0.0,
                        [(GPSCoordinate(49, 56, 32.25, "N"), GPSCoordinate(16, 54, 0.346, "E")),
                         (GPSCoordinate(50, 5, 17.752, "N"), GPSCoordinate(16, 55, 12.293, "E"))]),
        FishingLocation("473051", "MORAVICE 1 P", "MO OPAVA", 0.0,
                        [(GPSCoordinate(49, 54, 22.56, "N"), GPSCoordinate(17, 54, 29.299, "E")),
                         (GPSCoordinate(49, 51, 36.973, "N"), GPSCoordinate(17, 51, 41.339, "E"))]),
        FishingLocation("473052", "MORAVICE 2", "MO OPAVA", 0.0,
                        [(GPSCoordinate(49, 51, 37.008, "N"), GPSCoordinate(17, 51, 41.241, "E")),
                         (GPSCoordinate(49, 48, 33.335, "N"), GPSCoordinate(17, 47, 57.084, "E")),
                         (GPSCoordinate(49, 51, 4.548, "N"), GPSCoordinate(17, 50, 30.576, "E")),
                         (GPSCoordinate(49, 49, 52.754, "N"), GPSCoordinate(17, 49, 53.321, "E"))]),
        FishingLocation("473053", "MORAVICE 3 P", "MO VÍTKOV", 0.0,
                        [(GPSCoordinate(49, 48, 33.302, "N"), GPSCoordinate(17, 47, 57.082, "E")),
                         (GPSCoordinate(49, 49, 14.211, "N"), GPSCoordinate(17, 42, 58.307, "E"))]),
        FishingLocation("473054", "MORAVICE 4", "MO VÍTKOV", 0.0,
                        [(GPSCoordinate(49, 49, 14.211, "N"), GPSCoordinate(17, 42, 58.307, "E")),
                         (GPSCoordinate(49, 49, 27.52, "N"), GPSCoordinate(17, 40, 00.30, "E"))]),
        FishingLocation("473056", "MORAVICE 7", "MO RÝMAŘOV", 0.0,
                        [(GPSCoordinate(49, 55, 29.627, "N"), GPSCoordinate(17, 27, 8.222, "E")),
                         (GPSCoordinate(49, 56, 6.386, "N"), GPSCoordinate(17, 20, 44.715, "E"))]),
        FishingLocation("473057", "MORAVICE 8", "MO RÝMAŘOV", 0.0,
                        [(GPSCoordinate(49, 56, 6.534, "N"), GPSCoordinate(17, 20, 44.597, "E")),
                         (GPSCoordinate(50, 2, 20.397, "N"), GPSCoordinate(17, 15, 48.056, "E")),
                         (GPSCoordinate(50, 1, 29.757, "N"), GPSCoordinate(17, 15, 26.122, "E")),
                         (GPSCoordinate(50, 1, 53.162, "N"), GPSCoordinate(17, 14, 49.013, "E")),
                         (GPSCoordinate(50, 1, 36.472, "N"), GPSCoordinate(17, 16, 29.346, "E")),
                         (GPSCoordinate(50, 1, 17.104, "N"), GPSCoordinate(17, 14, 48.963, "E"))]),
        FishingLocation("473058", "MORÁVKA 1", "MO FRÝDEK-MÍSTEK", 0.0,
                        [(GPSCoordinate(49, 40, 19.13, "N"), GPSCoordinate(18, 21, 25.25, "E")),
                         (GPSCoordinate(49, 35, 08.36, "N"), GPSCoordinate(18, 31, 48.02, "E"))]),
        FishingLocation("473059", "ODRA 8", "MO VÍTKOV", 0.0,
                        [(GPSCoordinate(49, 40, 27.61, "N"), GPSCoordinate(17, 49, 04.23, "E")),
                         (GPSCoordinate(49, 44, 6.663, "N"), GPSCoordinate(17, 41, 37.734, "E"))]),
        FishingLocation("473061", "OLEŠNÁ 3", "MO FRÝDEK-MÍSTEK", 0.0,
                        [(GPSCoordinate(49, 39, 13.77, "N"), GPSCoordinate(18, 19, 19.97, "E")),
                         (GPSCoordinate(49, 35, 24.36, "N"), GPSCoordinate(18, 18, 45.28, "E"))]),
        FishingLocation("473062", "OLEŠNICE JESENICKÁ 1", "MO JESENÍK", 0.0, []),
        FishingLocation("473063", "OLEŠNICE PŘEROVSKÁ 2", "MO LIPNÍK NAD BEČVOU", 0.0,
                        [(GPSCoordinate(49, 30, 59.912, "N"), GPSCoordinate(17, 25, 21.586, "E")),
                         (GPSCoordinate(49, 32, 39.398, "N"), GPSCoordinate(17, 25, 34.072, "E"))]),
        FishingLocation("473064", "OLŠE 5 P", "MO TŘINEC", 0.0,
                        [(GPSCoordinate(49, 41, 4.303, "N"), GPSCoordinate(18, 39, 7.158, "E")),
                         (GPSCoordinate(49, 38, 28.076, "N"), GPSCoordinate(18, 42, 3.546, "E"))]),
        FishingLocation("473065", "OLŠE 6", "MO BYSTŘICE NAD OLŠÍ", 0.0,
                        [(GPSCoordinate(49, 38, 27.57, "N"), GPSCoordinate(18, 42, 3.657, "E")),
                         (GPSCoordinate(49, 36, 11.368, "N"), GPSCoordinate(18, 44, 14.901, "E"))]),
        FishingLocation("473066", "OLŠE 7", "MO JABLUNKOV", 0.0,
                        [(GPSCoordinate(49, 36, 11.369, "N"), GPSCoordinate(18, 44, 14.877, "E")),
                         (GPSCoordinate(49, 33, 40.979, "N"), GPSCoordinate(18, 50, 41.738, "E")),
                         (GPSCoordinate(49, 34, 53.491, "N"), GPSCoordinate(18, 44, 43.617, "E"))]),
        FishingLocation("473067", "ONDŘEJNICE 2", "MO STARÁ VES NAD ODŘEJNICÍ", 0.0,
                        [(GPSCoordinate(49, 43, 16.261, "N"), GPSCoordinate(18, 11, 41.435, "E")),
                         (GPSCoordinate(49, 40, 16.969, "N"), GPSCoordinate(18, 13, 34.24, "E"))]),
        FishingLocation("473068", "OPAVA 7", "MO KRNOV", 0.0,
                        [(GPSCoordinate(50, 5, 0.441, "N"), GPSCoordinate(17, 44, 10.561, "E")),
                         (GPSCoordinate(50, 1, 5.247, "N"), GPSCoordinate(17, 32, 34.073, "E"))]),
        FishingLocation("473069", "OPAVA 8", "MO BRUNTÁL", 0.0,
                        [(GPSCoordinate(50, 1, 5.264, "N"), GPSCoordinate(17, 32, 34.048, "E")),
                         (GPSCoordinate(50, 3, 49.286, "N"), GPSCoordinate(17, 28, 33.902, "E"))]),
        FishingLocation("473070", "OPAVICE (ZLATÁ) 1", "MO KRNOV", 0.0,
                        [(GPSCoordinate(50, 5, 45.907, "N"), GPSCoordinate(17, 42, 58.292, "E")),
                         (GPSCoordinate(50, 9, 45.497, "N"), GPSCoordinate(17, 34, 51.028, "E"))]),
        FishingLocation("473071", "OPAVICE (ZLATÁ) 2", "MO KRNOV", 0.0,
                        [(GPSCoordinate(50, 9, 45.805, "N"), GPSCoordinate(17, 34, 50.263, "E")),
                         (GPSCoordinate(50, 9, 45.905, "N"), GPSCoordinate(17, 28, 12.699, "E"))]),
        FishingLocation("473072", "OSKAVA 4", "MO UNIČOV", 0.0,
                        [(GPSCoordinate(49, 49, 6.518, "N"), GPSCoordinate(17, 6, 35.729, "E")),
                         (GPSCoordinate(49, 55, 51.027, "N"), GPSCoordinate(17, 9, 15.252, "E"))]),
        FishingLocation("473073", "OSLAVA ŠTERNBERSKÁ 1", "MO ŠTERNBERK", 0.0,
                        [(GPSCoordinate(49, 47, 44.678, "N"), GPSCoordinate(17, 7, 41.633, "E")),
                         (GPSCoordinate(49, 54, 40.897, "N"), GPSCoordinate(17, 17, 52.372, "E"))]),
        FishingLocation("473074", "OSOBLAHA 2", "MO KRNOV", 0.0,
                        [(GPSCoordinate(50, 14, 7.591, "N"), GPSCoordinate(17, 41, 3.221, "E")),
                         (GPSCoordinate(50, 12, 41.554, "N"), GPSCoordinate(17, 25, 25.808, "E"))]),
        FishingLocation("473075", "OSTRAVICE 3", "MO FRÝDEK-MÍSTEK", 0.0,
                        [(GPSCoordinate(49, 41, 16.761, "N"), GPSCoordinate(18, 19, 57.518, "E")),
                         (GPSCoordinate(49, 36, 27.186, "N"), GPSCoordinate(18, 21, 32.279, "E")),
                         (GPSCoordinate(49, 39, 50.507, "N"), GPSCoordinate(18, 21, 44.99, "E")),
                         (GPSCoordinate(49, 37, 36.624, "N"), GPSCoordinate(18, 26, 0.178, "E"))]),
        FishingLocation("473076", "OSTRAVICE 4", "MO FRÝDLANT NAD OSTRAVICÍ", 0.0,
                        [(GPSCoordinate(49, 36, 27.095, "N"), GPSCoordinate(18, 21, 32.348, "E")),
                         (GPSCoordinate(49, 30, 44.755, "N"), GPSCoordinate(18, 24, 56.071, "E"))]),
        FishingLocation("473077", "OSTRAVICE 6", "MO FRÝDLANT NAD OSTRAVICÍ", 0.0,
                        [(GPSCoordinate(49, 27, 40.517, "N"), GPSCoordinate(18, 27, 5.243, "E")),
                         (GPSCoordinate(49, 24, 57.198, "N"), GPSCoordinate(18, 22, 20.317, "E")),
                         (GPSCoordinate(49, 28, 25.389, "N"), GPSCoordinate(18, 25, 38.954, "E")),
                         (GPSCoordinate(49, 28, 28.127, "N"), GPSCoordinate(18, 23, 59.708, "E"))]),
        FishingLocation("473078", "PODOLSKÝ POTOK 1", "MO RÝMAŘOV", 0.0,
                        [(GPSCoordinate(49, 56, 6.405, "N"), GPSCoordinate(17, 20, 44.566, "E")),
                         (GPSCoordinate(49, 56, 44.076, "N"), GPSCoordinate(17, 15, 10.223, "E"))]),
        FishingLocation("473079", "POLICKÝ POTOK", "MO MOHELNICE", 0.0,
                        [(GPSCoordinate(49, 47, 20.434, "N"), GPSCoordinate(16, 57, 50.671, "E")),
                         (GPSCoordinate(49, 52, 15.536, "N"), GPSCoordinate(17, 2, 0.552, "E"))]),
        FishingLocation("473080", "RAČÍ POTOK", "MO JAVORNÍK", 0.0,
                        [(GPSCoordinate(50, 24, 24.792, "N"), GPSCoordinate(17, 3, 11.323, "E")),
                         (GPSCoordinate(50, 20, 38.34, "N"), GPSCoordinate(16, 58, 19.583, "E")),
                         (GPSCoordinate(50, 24, 19.858, "N"), GPSCoordinate(17, 5, 0.37, "E")),
                         (GPSCoordinate(50, 18, 48.917, "N"), GPSCoordinate(16, 58, 53.46, "E"))]),
        FishingLocation("473081", "ROKYTENKA 1", "MO VSETÍN", 0.0,
                        [(GPSCoordinate(49, 20, 28.532, "N"), GPSCoordinate(17, 59, 23.017, "E")),
                         (GPSCoordinate(49, 17, 27.966, "N"), GPSCoordinate(17, 55, 30.243, "E"))]),
        FishingLocation("473082", "ROPIČANKA 1", "MO ČESKÝ TĚŠÍN", 0.0,
                        [(GPSCoordinate(49, 43, 42.3, "N"), GPSCoordinate(18, 37, 35.215, "E")),
                         (GPSCoordinate(49, 36, 1.807, "N"), GPSCoordinate(18, 35, 22.061, "E"))]),
        FishingLocation("473083", "SÁZAVA MORAVSKÁ 2 P", "MO ZÁBŘEH NA MORAVĚ", 0.0,
                        [(GPSCoordinate(49, 52, 3.856, "N"), GPSCoordinate(16, 50, 43.588, "E")),
                         (GPSCoordinate(49, 51, 55.254, "N"), GPSCoordinate(16, 44, 47.624, "E"))]),
        FishingLocation("473084", "SEDLNIČKA 1", "MO PŘÍBOR", 0.0,
                        [(GPSCoordinate(49, 42, 1.864, "N"), GPSCoordinate(18, 4, 0.595, "E")),
                         (GPSCoordinate(49, 35, 6.5, "N"), GPSCoordinate(18, 6, 7.623, "E"))]),
        FishingLocation("473085", "SENICE 1", "MO VSETÍN", 0.0,
                        [(GPSCoordinate(49, 18, 44.876, "N"), GPSCoordinate(18, 0, 5.286, "E")),
                         (GPSCoordinate(49, 15, 37.908, "N"), GPSCoordinate(18, 9, 25.074, "E"))]),
        FishingLocation("473086", "SETINA 1", "MO BÍLOVEC", 0.0,
                        [(GPSCoordinate(49, 44, 37.419, "N"), GPSCoordinate(18, 5, 18.079, "E")),
                         (GPSCoordinate(49, 49, 36.854, "N"), GPSCoordinate(17, 56, 43.563, "E"))]),
        FishingLocation("473087", "SITKA 2", "MO ŠTERNBERK", 0.0,
                        [(GPSCoordinate(49, 43, 25.952, "N"), GPSCoordinate(17, 17, 9.764, "E")),
                         (GPSCoordinate(49, 50, 48.031, "N"), GPSCoordinate(17, 19, 46.422, "E")),
                         (GPSCoordinate(49, 47, 5.43, "N"), GPSCoordinate(17, 11, 40.236, "E")),
                         (GPSCoordinate(49, 48, 43.533, "N"), GPSCoordinate(17, 16, 7.678, "E"))]),
        FishingLocation("473088", "SKOROŠICKÝ POTOK 1", "MO JAVORNÍK", 0.0,
                        [(GPSCoordinate(50, 20, 17.489, "N"), GPSCoordinate(17, 7, 4.922, "E")),
                         (GPSCoordinate(50, 17, 41.241, "N"), GPSCoordinate(17, 1, 54.515, "E"))]),
        FishingLocation("473089", "STAŘÍČ 1", "MO JESENÍK", 0.0,
                        [(GPSCoordinate(50, 14, 9.999, "N"), GPSCoordinate(17, 12, 12.921, "E")),
                         (GPSCoordinate(50, 13, 30.164, "N"), GPSCoordinate(17, 6, 36.664, "E"))]),
        FishingLocation("473090", "STONÁVKA 1 P", "MO KARVINÁ", 0.0,
                        [(GPSCoordinate(49, 49, 31.987, "N"), GPSCoordinate(18, 31, 31.945, "E")),
                         (GPSCoordinate(49, 46, 26.671, "N"), GPSCoordinate(18, 31, 3.65, "E"))]),
        FishingLocation("473091", "STONÁVKA 3", "MO ČESKÝ TĚŠÍN", 0.0,
                        [(GPSCoordinate(49, 44, 0.456, "N"), GPSCoordinate(18, 29, 46.378, "E")),
                         (GPSCoordinate(49, 37, 32.425, "N"), GPSCoordinate(18, 31, 2.09, "E")),
                         (GPSCoordinate(49, 39, 40.19, "N"), GPSCoordinate(18, 31, 30.27, "E")),
                         (GPSCoordinate(49, 37, 3.335, "N"), GPSCoordinate(18, 33, 23.571, "E"))]),
        FishingLocation("473092", "ŠUMICE 1 P", "MO OLOMOUC", 0.0,
                        [(GPSCoordinate(49, 36, 8.187, "N"), GPSCoordinate(17, 3, 53.444, "E")),
                         (GPSCoordinate(49, 37, 7.039, "N"), GPSCoordinate(16, 58, 29.079, "E"))]),
        FishingLocation("473093", "TRNÁVKA 1", "MO STARÁ VES NAD ONDŘEJNICÍ", 0.0,
                        [(GPSCoordinate(49, 43, 26.496, "N"), GPSCoordinate(18, 10, 0.69, "E")),
                         (GPSCoordinate(49, 39, 16.834, "N"), GPSCoordinate(18, 10, 1.702, "E"))]),
        FishingLocation("473094", "TRUSOVICKÝ POTOK 1", "MO DOMAŠOV NAD BYSTŘICÍ", 0.0,
                        [(GPSCoordinate(49, 39, 14.743, "N"), GPSCoordinate(17, 16, 41.126, "E")),
                         (GPSCoordinate(49, 46, 12.635, "N"), GPSCoordinate(17, 22, 40.988, "E")),
                         (GPSCoordinate(49, 46, 17.145, "N"), GPSCoordinate(17, 21, 50.731, "E")),
                         (GPSCoordinate(49, 46, 38.259, "N"), GPSCoordinate(17, 20, 41.472, "E"))]),
        FishingLocation("473095", "TYRA 1", "MO TŘINEC", 0.0,
                        [(GPSCoordinate(49, 40, 58.962, "N"), GPSCoordinate(18, 39, 22.408, "E")),
                         (GPSCoordinate(49, 34, 58.268, "N"), GPSCoordinate(18, 37, 48.94, "E"))]),
        FishingLocation("473096", "VELIČKA 1", "MO HRANICE", 0.0,
                        [(GPSCoordinate(49, 32, 45.097, "N"), GPSCoordinate(17, 43, 47.345, "E")),
                         (GPSCoordinate(49, 38, 2.066, "N"), GPSCoordinate(17, 38, 23.547, "E"))]),
        FishingLocation("473097", "VIDNÁVKA 1", "MO JAVORNÍK", 0.0,
                        [(GPSCoordinate(50, 23, 19.999, "N"), GPSCoordinate(17, 11, 27.284, "E")),
                         (GPSCoordinate(50, 15, 15.816, "N"), GPSCoordinate(17, 9, 25.475, "E"))]),
        FishingLocation("473098", "OPAVA 9", "MO VRBNO POD PRADĚDEM", 0.0,
                        [(GPSCoordinate(50, 3, 49.598, "N"), GPSCoordinate(17, 28, 34.447, "E")),
                         (GPSCoordinate(50, 7, 29.437, "N"), GPSCoordinate(17, 22, 3.982, "E"))]),
        FishingLocation("473099", "PRUDNÍK 2 P", "MO ZLATÉ HORY", 0.0,
                        [(GPSCoordinate(50, 16, 44.709, "N"), GPSCoordinate(17, 24, 4.947, "E")),
                         (GPSCoordinate(50, 15, 46.588, "N"), GPSCoordinate(17, 23, 37.244, "E"))]),
        FishingLocation("473101", "STŘÍBRNÝ POTOK 1", "MO JAVORNÍK", 0.0,
                        [(GPSCoordinate(50, 18, 41.648, "N"), GPSCoordinate(17, 6, 7.542, "E")),
                         (GPSCoordinate(50, 16, 26.042, "N"), GPSCoordinate(17, 3, 7.91, "E"))]),
        FishingLocation("473102", "MÍROVKA 1", "MO MOHELNICE", 0.0,
                        [(GPSCoordinate(49, 46, 58.926, "N"), GPSCoordinate(16, 57, 21.394, "E")),
                         (GPSCoordinate(49, 47, 2.462, "N"), GPSCoordinate(16, 46, 35.743, "E"))]),
        FishingLocation("473103", "MORÁVKA 2 P", "MO FRÝDEK-MÍSTEK", 0.0,
                        [(GPSCoordinate(49, 33, 34.49, "N"), GPSCoordinate(18, 32, 59.80, "E")),
                         (GPSCoordinate(49, 30, 07.80, "N"), GPSCoordinate(18, 32, 34.85, "E"))]),
        FishingLocation("473104", "OSTRAVICE 2", "MO ČRS OSTRAVA", 0.0,
                        [(GPSCoordinate(49, 48, 9.636, "N"), GPSCoordinate(18, 16, 56.843, "E")),
                         (GPSCoordinate(49, 41, 45.290, "N"), GPSCoordinate(18, 19, 40.596, "E"))]),
        FishingLocation("473105", "MOŠTĚNKA 2", "MO ČRS PŘEROV", 0.0,
                        [(GPSCoordinate(49, 25, 43.708, "N"), GPSCoordinate(17, 30, 45.552, "E")),
                         (GPSCoordinate(49, 25, 31.459, "N"), GPSCoordinate(17, 32, 51.237, "E")),
                         (GPSCoordinate(49, 25, 29.583, "N"), GPSCoordinate(17, 32, 40.465, "E")),
                         (GPSCoordinate(49, 22, 58.248, "N"), GPSCoordinate(17, 40, 32.452, "E"))]),
        FishingLocation("473106", "OPAVA 9 P", "MO VRBNO POD PRADĚDEM", 0.10,
                        [(GPSCoordinate(50, 7, 1.565, "N"), GPSCoordinate(17, 23, 32.34, "E"))]),
        FishingLocation("473108", "JIČÍNKA 1P", "MO NOVÝ JIČÍN", 0.0,
                        [(GPSCoordinate(49, 39, 56.676, "N"), GPSCoordinate(17, 59, 32.545, "E")),
                         (GPSCoordinate(49, 37, 34.954, "N"), GPSCoordinate(17, 59, 29.164, "E"))]),
        FishingLocation("473300", "BEČVA ROŽNOVSKÁ 1", "MO VALAŠSKÉ MEZIŘÍČÍ   CH A P", 0.0, []),
        FishingLocation("473301", "ČERNÝ POTOK 1", "MO BRUNTÁL", 0.0,
                        [(GPSCoordinate(49, 57, 53.563, "N"), GPSCoordinate(17, 29, 16.402, "E")),
                         (GPSCoordinate(50, 2, 1.573, "N"), GPSCoordinate(17, 23, 52.095, "E"))]),
        FishingLocation("473500", "STŘEDNÍ OPAVA 1", "MO VRBNO P. PRADĚDEM", 0.0, []),
    ]
