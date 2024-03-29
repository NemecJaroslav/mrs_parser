from production_code.common.fishing_location import FishingLocation
from production_code.common.parser import GPSCoordinate


def get_expected_fishing_locations():
    return [
        FishingLocation("463001", "KŘTINSKÝ POTOK", "ADAMOV", 2.0, []),
        FishingLocation("463002", "BĚLÁ BOSKOVICKÁ 1", "BOSKOVICE", 4.2,
                        [(GPSCoordinate(49, 28, 19.30, "N"), GPSCoordinate(16, 37, 16.21, "E")),
                         (GPSCoordinate(49, 29, 34.8, "N"), GPSCoordinate(16, 41, 51.60, "E"))]),
        FishingLocation("463003", "BESÉNEK 1", "TIŠNOV", 5.0, []),
        FishingLocation("463004", "BÍLÁ VODA", "BLANSKO", 4.0, []),
        FishingLocation("463032", "BÍLÝ POTOK 1", "VEVERSKÁ BÍTÝŠKA", 1.5,
                        [(GPSCoordinate(49, 16, 40.80, "N"), GPSCoordinate(16, 26, 16.99, "E")),
                         (GPSCoordinate(49, 15, 44.85, "N"), GPSCoordinate(16, 23, 48.97, "E"))]),
        FishingLocation("463005", "BÍLÝ POTOK 2", "VELKÁ BÍTEŠ", 9.3,
                        [(GPSCoordinate(49, 15, 44.85, "N"), GPSCoordinate(16, 23, 48.97, "E")),
                         (GPSCoordinate(49, 19, 03.80, "N"), GPSCoordinate(16, 10, 22.19, "E"))]),
        FishingLocation("463006", "BISKUPICKÝ POTOK 1", "UHERSKÝ BROD", 3.0,
                        [(GPSCoordinate(49, 4, 29.72, "N"), GPSCoordinate(17, 42, 48.26, "E")),
                         (GPSCoordinate(49, 7, 14.97, "N"), GPSCoordinate(17, 41, 21.13, "E")),
                         (GPSCoordinate(49, 4, 29.49, "N"), GPSCoordinate(17, 42, 48.39, "E")),
                         (GPSCoordinate(49, 7, 20.47, "N"), GPSCoordinate(17, 43, 38.59, "E"))]),
        FishingLocation("463008", "BŘEZNICE 1", "UHERSKÉ HRADIŠTĚ", 4.0,
                        [(GPSCoordinate(49, 5, 26.02, "N"), GPSCoordinate(17, 29, 47.70, "E")),
                         (GPSCoordinate(49, 9, 48.60, "N"), GPSCoordinate(17, 38, 11.52, "E")),
                         (GPSCoordinate(49, 6, 5.40, "N"), GPSCoordinate(17, 33, 13.35, "E")),
                         (GPSCoordinate(49, 6, 22.15, "N"), GPSCoordinate(17, 35, 59.96, "E"))]),
        FishingLocation("463009", "BŘEZOVSKÝ POTOK 1", "UHERSKÝ BROD", 2.0, []),
        FishingLocation("463010", "BÝKOVKA 1", "BLANSKO", 3.0, []),
        FishingLocation("463011", "BYSTŘICE HOSTÝNSKÁ 1", "BYSTŘICE POD HOSTÝNEM", 2.0,
                        [(GPSCoordinate(49, 25, 47.05, "N"), GPSCoordinate(17, 35, 46.56, "E")),
                         (GPSCoordinate(49, 22, 41.05, "N"), GPSCoordinate(17, 43, 16.77, "E"))]),
        FishingLocation("463012", "BYSTŘICE PERNŠTEJNSKÁ 1", "BYSTŘICE NAD PERNŠTEJNEM", 5.0,
                        [(GPSCoordinate(49, 33, 25.00, "N"), GPSCoordinate(16, 18, 55.74, "E")),
                         (GPSCoordinate(49, 32, 40.30, "N"), GPSCoordinate(16, 12, 15.37, "E"))]),
        FishingLocation("463013", "CIKHÁJSKÝ POTOK 2", "ŽĎÁR NAD SÁZAVOU", 1.0, []),
        FishingLocation("463014", "DŘEVNICE SLUŠOVICKÁ 1", "ZLÍN", 4.0,
                        [(GPSCoordinate(49, 13, 4.637, "N"), GPSCoordinate(17, 46, 40.884, "E")),
                         (GPSCoordinate(49, 19, 13.154, "N"), GPSCoordinate(17, 46, 50.218, "E")),
                         (GPSCoordinate(49, 19, 19.280, "N"), GPSCoordinate(17, 47, 33.645, "E")),
                         (GPSCoordinate(49, 18, 10.76, "N"), GPSCoordinate(17, 45, 59.55, "E")),
                         (GPSCoordinate(49, 17, 6.54, "N"), GPSCoordinate(17, 53, 31.36, "E")),
                         (GPSCoordinate(49, 17, 55.52, "N"), GPSCoordinate(17, 50, 39.11, "E"))]),
        FishingLocation("463015", "DŘEVNICE VIZOVICKÁ 1", "ZLÍN", 20.0,
                        [(GPSCoordinate(49, 13, 16.04, "N"), GPSCoordinate(17, 42, 54.71, "E")),
                         (GPSCoordinate(49, 13, 16.77, "N"), GPSCoordinate(17, 50, 58.59, "E")),
                         (GPSCoordinate(49, 13, 33.895, "N"), GPSCoordinate(17, 54, 49.109, "E")),
                         (GPSCoordinate(49, 13, 16.8, "N"), GPSCoordinate(17, 50, 58.7, "E")),
                         (GPSCoordinate(49, 14, 20.08, "N"), GPSCoordinate(17, 52, 56.90, "E")),
                         (GPSCoordinate(49, 14, 27.47, "N"), GPSCoordinate(17, 44, 31.38, "E")),
                         (GPSCoordinate(49, 11, 45.66, "N"), GPSCoordinate(17, 44, 31.26, "E"))]),
        FishingLocation("463017", "DYJE 12", "ZNOJMO", 49.0, []),
        FishingLocation("463016", "DYJE 12A", "ZNOJMO", 12.0,
                        [(GPSCoordinate(48, 50, 19.722, "N"), GPSCoordinate(15, 59, 46.569, "E")),
                         (GPSCoordinate(48, 49, 11.51, "N"), GPSCoordinate(15, 57, 34.93, "E"))]),
        FishingLocation("463018", "DYJE 13/1", "ZNOJMO", 17.0,
                        [(GPSCoordinate(48, 49, 33.51, "N"), GPSCoordinate(15, 56, 23.34, "E")),
                         (GPSCoordinate(48, 50, 9.07, "N"), GPSCoordinate(15, 54, 22.22, "E"))]),
        FishingLocation("463018", "DYJE 13/2", "ZNOJMO", 8.0,
                        [(GPSCoordinate(48, 50, 56.69, "N"), GPSCoordinate(15, 53, 35.92, "E")),
                         (GPSCoordinate(48, 51, 11.48, "N"), GPSCoordinate(15, 52, 51.71, "E"))]),
        FishingLocation("463018", "DYJE 13/3", "ZNOJMO", 11.0,
                        [(GPSCoordinate(48, 51, 29.53, "N"), GPSCoordinate(15, 52, 25.28, "E")),
                         (GPSCoordinate(48, 51, 44.00, "N"), GPSCoordinate(15, 50, 32.73, "E"))]),
        FishingLocation("463019", "DYJE 14", "VRANOV NAD DYJÍ", 22.0,
                        [(GPSCoordinate(48, 52, 32.77, "N"), GPSCoordinate(15, 50, 42.26, "E")),
                         (GPSCoordinate(48, 54, 24.26, "N"), GPSCoordinate(15, 49, 9.81, "E"))]),
        FishingLocation("463020", "DYJE 20", "TELČ", 2.2,
                        [(GPSCoordinate(49, 9, 38.65, "N"), GPSCoordinate(15, 28, 26.31, "E")),
                         (GPSCoordinate(49, 12, 48.09, "N"), GPSCoordinate(15, 30, 44.30, "E"))]),
        FishingLocation("463021", "FRYŠÁVKA 1", "NOVÉ MĚSTO NA MORAVĚ", 5.0,
                        [(GPSCoordinate(49, 38, 19.68, "N"), GPSCoordinate(16, 13, 26.05, "E")),
                         (GPSCoordinate(49, 37, 57.32, "N"), GPSCoordinate(16, 4, 30.65, "E"))]),
        FishingLocation("463022", "HANÁ 4", "VYŠKOV", 3.0,
                        [(GPSCoordinate(49, 16, 55.93, "N"), GPSCoordinate(16, 59, 41.22, "E")),
                         (GPSCoordinate(49, 19, 58.05, "N"), GPSCoordinate(16, 55, 57.21, "E"))]),
        FishingLocation("463023", "HLOUČELA 1P", "PROSTĚJOV", 3.0,
                        [(GPSCoordinate(49, 28, 33.45, "N"), GPSCoordinate(17, 8, 50.31, "E")),
                         (GPSCoordinate(49, 28, 5.45, "N"), GPSCoordinate(17, 2, 23.11, "E"))]),
        FishingLocation("463024", "HODONÍNKA 1", "NEDVĚDICE", 4.0, []),
        FishingLocation("463083", "HORNÍ RYBNÍK", "BOSKOVICE", 0.5,
                        [(GPSCoordinate(49, 28, 46.509, "N"), GPSCoordinate(16, 39, 16.0488, "E"))]),
        FishingLocation("463025", "CHVOJNICE 1", "NÁMĚŠŤ NAD OSLAVOU", 3.0, []),
        FishingLocation("463026", "CHVOJNICE 2", "VELKÁ BÍTEŠ", 2.0, []),
        FishingLocation("463048", "JANUŠTICE 1", "ZLÍN", 2.5,
                        [(GPSCoordinate(49, 13, 48.17, "N"), GPSCoordinate(17, 40, 50.02, "E")),
                         (GPSCoordinate(49, 15, 50.61, "N"), GPSCoordinate(17, 41, 28.72, "E"))]),
        FishingLocation("463027", "JIHLAVA 5A", "IVANČICE", 15.3,
                        [(GPSCoordinate(49, 5, 50.94, "N"), GPSCoordinate(16, 21, 51.57, "E")),
                         (GPSCoordinate(49, 5, 49.75, "N"), GPSCoordinate(16, 18, 08.09, "E"))]),
        FishingLocation("463028", "JIHLAVA 5B", "NOVÁ VES U OSLAVAN", 19.8,
                        [(GPSCoordinate(49, 5, 49.75, "N"), GPSCoordinate(16, 18, 08.09, "E")),
                         (GPSCoordinate(49, 6, 1.969, "N"), GPSCoordinate(16, 12, 37.405, "E")),
                         (GPSCoordinate(49, 5, 59.87, "N"), GPSCoordinate(16, 14, 28.32, "E")),
                         (GPSCoordinate(49, 6, 1.969, "N"), GPSCoordinate(16, 12, 37.405, "E"))]),
        FishingLocation("463029", "JIHLAVA 5C", "MOHELNO", 8.0,
                        [(GPSCoordinate(49, 6, 1.79, "N"), GPSCoordinate(16, 12, 37.41, "E")),
                         (GPSCoordinate(49, 6, 10.6, "N"), GPSCoordinate(16, 10, 57.2, "E"))]),
        FishingLocation("463030", "KLANEČNICE 1", "UHERSKÝ BROD", 1.0,
                        [(GPSCoordinate(48, 52, 43.17, "N"), GPSCoordinate(17, 43, 48.71, "E")),
                         (GPSCoordinate(48, 54, 26.34, "N"), GPSCoordinate(17, 40, 32.49, "E")),
                         (GPSCoordinate(48, 53, 04.52, "N"), GPSCoordinate(17, 43, 21.39, "E")),
                         (GPSCoordinate(48, 52, 56.73, "N"), GPSCoordinate(17, 42, 46.19, "E"))]),
        FishingLocation("463031", "KLAPŮVKA", "TŘEBÍČ", 3.0, []),
        FishingLocation("463049", "KLOBOUČKA 1", "SLAVIČÍN", 6.0,
                        [(GPSCoordinate(49, 4, 03.46, "N"), GPSCoordinate(18, 0, 11.97, "E")),
                         (GPSCoordinate(49, 9, 03.14, "N"), GPSCoordinate(18, 5, 34.01, "E"))]),
        FishingLocation("463033", "KOTOJEDKA 1", "KROMĚŘÍŽ", 3.0,
                        [(GPSCoordinate(49, 17, 11.88, "N"), GPSCoordinate(17, 25, 40.38, "E")),
                         (GPSCoordinate(49, 9, 41.45, "N"), GPSCoordinate(17, 16, 04.70, "E"))]),
        FishingLocation("463034", "KŘETÍNKA 1P", "LETOVICE", 3.0,
                        [(GPSCoordinate(49, 33, 58.40, "N"), GPSCoordinate(16, 30, 22.37, "E")),
                         (GPSCoordinate(49, 35, 27.77, "N"), GPSCoordinate(16, 28, 12.41, "E"))]),
        FishingLocation("463035", "KUDLOVICKÝ POTOK 1", "UHERSKÉ HRADIŠTĚ", 2.0,
                        [(GPSCoordinate(49, 6, 54.14, "N"), GPSCoordinate(17, 29, 21.09, "E")),
                         (GPSCoordinate(49, 11, 29.27, "N"), GPSCoordinate(17, 24, 03.17, "E"))]),
        FishingLocation("463036", "KYJOVKA 4", "OSVĚTIMANY", 3.0,
                        [(GPSCoordinate(49, 6, 43.48, "N"), GPSCoordinate(17, 8, 25.12, "E")),
                         (GPSCoordinate(49, 7, 30.14, "N"), GPSCoordinate(17, 15, 31.42, "E"))]),
        FishingLocation("463037", "LIBOCHŮVKA 1", "DOLNÍ LOUČKY", 8.0,
                        [(GPSCoordinate(49, 21, 36.93, "N"), GPSCoordinate(16, 21, 20.78, "E")),
                         (GPSCoordinate(49, 24, 19.85, "N"), GPSCoordinate(16, 13, 21.42, "E"))]),
        FishingLocation("463038", "LÍŠEŇSKÁ ŘÍČKA 2", "BRNO 4", 7.0,
                        [(GPSCoordinate(49, 13, 15.92, "N"), GPSCoordinate(16, 42, 50.86, "E")),
                         (GPSCoordinate(49, 15, 05.86, "N"), GPSCoordinate(16, 45, 50.74, "E")),
                         (GPSCoordinate(49, 13, 15.92, "N"), GPSCoordinate(16, 42, 50.86, "E")),
                         (GPSCoordinate(49, 13, 59.0, "N"), GPSCoordinate(16, 43, 23.1, "E")),
                         (GPSCoordinate(49, 14, 54.1, "N"), GPSCoordinate(16, 45, 31.6, "E"))]),
        FishingLocation("463039", "LOUČKA 1", "DOLNÍ LOUČKY", 16.7,
                        [(GPSCoordinate(49, 21, 23.88, "N"), GPSCoordinate(16, 24, 16.61, "E")),
                         (GPSCoordinate(49, 25, 17.97, "N"), GPSCoordinate(16, 14, 34.99, "E"))]),
        FishingLocation("463040", "LOUČKA 2", "DOLNÍ ROŽÍNKA", 6.0,
                        [(GPSCoordinate(49, 25, 17.97, "N"), GPSCoordinate(16, 14, 34.99, "E")),
                         (GPSCoordinate(49, 27, 18.59, "N"), GPSCoordinate(16, 10, 43.13, "E"))]),
        FishingLocation("463041", "LOUČKA 3", "DOLNÍ ROŽÍNKA", 5.8,
                        [(GPSCoordinate(49, 27, 18.59, "N"), GPSCoordinate(16, 10, 43.13, "E")),
                         (GPSCoordinate(49, 28, 37.77, "N"), GPSCoordinate(16, 7, 04.08, "E"))]),
        FishingLocation("463042", "LOUČKA 4", "NOVÉ MĚSTO NA MORAVĚ", 6.5,
                        [(GPSCoordinate(49, 28, 37.77, "N"), GPSCoordinate(16, 7, 04.08, "E")),
                         (GPSCoordinate(49, 33, 24.72, "N"), GPSCoordinate(16, 4, 15.85, "E"))]),
        FishingLocation("463043", "LUBĚ 1", "TIŠNOV", 5.0, []),
        FishingLocation("463082", "MALÁ JIHLÁVKA 1", "JIHLAVA", 3.2,
                        [(GPSCoordinate(49, 23, 14.90, "N"), GPSCoordinate(15, 36, 20.22, "E")),
                         (GPSCoordinate(49, 19, 55.46, "N"), GPSCoordinate(15, 34, 37.90, "E"))]),
        FishingLocation("463044", "MOJENA 1", "HOLEŠOV", 2.1,
                        [(GPSCoordinate(49, 17, 37.57, "N"), GPSCoordinate(17, 29, 12.37, "E")),
                         (GPSCoordinate(49, 20, 0.45, "N"), GPSCoordinate(17, 39, 53.49, "E"))]),
        FishingLocation("463045", "MOŠTĚNKA 2", "BYSTŘICE POD HOSTÝNEM", 7.0,
                        [(GPSCoordinate(49, 25, 29.94, "N"), GPSCoordinate(17, 32, 49.07, "E")),
                         (GPSCoordinate(49, 26, 13.11, "N"), GPSCoordinate(17, 43, 56.69, "E")),
                         (GPSCoordinate(49, 26, 58.77, "N"), GPSCoordinate(17, 38, 08.82, "E")),
                         (GPSCoordinate(49, 25, 13.98, "N"), GPSCoordinate(17, 41, 41.65, "E")),
                         (GPSCoordinate(49, 26, 38.35, "N"), GPSCoordinate(17, 38, 40.90, "E")),
                         (GPSCoordinate(49, 25, 8.42, "N"), GPSCoordinate(17, 42, 55.91, "E")),
                         (GPSCoordinate(49, 26, 11.64, "N"), GPSCoordinate(17, 36, 24.98, "E")),
                         (GPSCoordinate(49, 28, 33.45, "N"), GPSCoordinate(17, 40, 23.77, "E"))]),
        FishingLocation("463046", "NEDVĚDIČKA 1", "NEDVĚDICE", 5.6, []),
        FishingLocation("463081", "NIVNIČKA 1", "UHERSKÝ BROD", 5.0,
                        [(GPSCoordinate(49, 1, 06.42, "N"), GPSCoordinate(17, 39, 12.14, "E")),
                         (GPSCoordinate(48, 58, 1.93, "N"), GPSCoordinate(17, 43, 55.89, "E"))]),
        FishingLocation("463047", "OLEŠNICKÝ POTOK 1", "OLEŠNICE NA MORAVĚ", 3.2,
                        [(GPSCoordinate(49, 30, 09.86, "N"), GPSCoordinate(16, 24, 29.07, "E")),
                         (GPSCoordinate(49, 35, 20.05, "N"), GPSCoordinate(16, 22, 48.36, "E")),
                         (GPSCoordinate(49, 32, 41.527, "N"), GPSCoordinate(16, 25, 51.293, "E")),
                         (GPSCoordinate(49, 34, 2.11, "N"), GPSCoordinate(16, 24, 47.01, "E"))]),
        FishingLocation("463050", "OLŠAVA 3", "BOJKOVICE", 2.9,
                        [(GPSCoordinate(49, 1, 5.114, "N"), GPSCoordinate(17, 45, 21.501, "E")),
                         (GPSCoordinate(49, 1, 32.41, "N"), GPSCoordinate(17, 52, 47.12, "E")),
                         (GPSCoordinate(48, 59, 55.89, "N"), GPSCoordinate(17, 47, 45.80, "E")),
                         (GPSCoordinate(49, 1, 29.29, "N"), GPSCoordinate(17, 49, 19.34, "E")),
                         (GPSCoordinate(49, 2, 02.68, "N"), GPSCoordinate(17, 46, 00.00, "E")),
                         (GPSCoordinate(49, 1, 24.21, "N"), GPSCoordinate(17, 47, 11.79, "E")),
                         (GPSCoordinate(49, 2, 2.46, "N"), GPSCoordinate(17, 47, 35.47, "E"))]),
        FishingLocation("463052", "OSLAVA 6", "VELKÉ MEZIŘÍČÍ", 7.0,
                        [(GPSCoordinate(49, 18, 30.62, "N"), GPSCoordinate(16, 1, 54.45, "E")),
                         (GPSCoordinate(49, 23, 37.73, "N"), GPSCoordinate(16, 0, 46.46, "E"))]),
        FishingLocation("463053", "RADĚJOVSKÝ POTOK 1", "STRÁŽNICE", 3.0,
                        [(GPSCoordinate(48, 52, 48.98, "N"), GPSCoordinate(17, 16, 30.70, "E")),
                         (GPSCoordinate(48, 50, 45.96, "N"), GPSCoordinate(17, 26, 20.94, "E"))]),
        FishingLocation("463054", "RAKOVEC 3", "VYŠKOV", 1.0,
                        [(GPSCoordinate(49, 16, 22.64, "N"), GPSCoordinate(16, 53, 54.95, "E")),
                         (GPSCoordinate(49, 17, 32.96, "N"), GPSCoordinate(16, 51, 51.04, "E"))]),
        FishingLocation("463055", "RUSAVA 1", "HOLEŠOV", 1.0,
                        [(GPSCoordinate(49, 19, 21.81, "N"), GPSCoordinate(17, 29, 59.59, "E")),
                         (GPSCoordinate(49, 21, 15.74, "N"), GPSCoordinate(17, 42, 06.64, "E"))]),
        FishingLocation("463056", "RYBNICKÝ POTOK 1", "VESELÍ NAD MORAVOU", 1.0,
                        [(GPSCoordinate(48, 49, 15.61, "N"), GPSCoordinate(17, 30, 38.90, "E")),
                         (GPSCoordinate(48, 49, 11.28, "N"), GPSCoordinate(17, 32, 48.46, "E"))]),
        FishingLocation("463057", "SÁZAVA 16", "ŽĎÁR NAD SÁZAVOU", 12.0,
                        [(GPSCoordinate(49, 33, 48.39, "N"), GPSCoordinate(15, 46, 37.62, "E")),
                         (GPSCoordinate(49, 33, 54.24, "N"), GPSCoordinate(15, 53, 56.84, "E")),
                         (GPSCoordinate(49, 34, 14.36, "N"), GPSCoordinate(15, 46, 7.56, "E")),
                         (GPSCoordinate(49, 34, 56.65, "N"), GPSCoordinate(15, 49, 52.53, "E"))]),
        FishingLocation("463058", "SEMÍČ 1", "BOSKOVICE", 1.6, []),
        FishingLocation("463059", "STAROHROZENKOVSKÝ POTOK 1", "BOJKOVICE", 1.55,
                        [(GPSCoordinate(48, 57, 05.54, "N"), GPSCoordinate(17, 53, 44.13, "E")),
                         (GPSCoordinate(48, 58, 6.19, "N"), GPSCoordinate(17, 50, 26.61, "E")),
                         (GPSCoordinate(48, 57, 32.51, "N"), GPSCoordinate(17, 52, 36.19, "E"))]),
        FishingLocation("463060", "STAVIŠTĚ 1", "ŽĎÁR NAD SÁZAVOU", 1.0, []),
        FishingLocation("463061", "SUDOMĚŘICKÝ POTOK 1", "HODONÍN", 2.0,
                        [(GPSCoordinate(48, 52, 17.83, "N"), GPSCoordinate(17, 13, 31.25, "E")),
                         (GPSCoordinate(48, 50, 35.20, "N"), GPSCoordinate(17, 20, 30.87, "E"))]),
        FishingLocation("463063", "SVITAVA 2", "ADAMOV", 32.0,
                        [(GPSCoordinate(49, 15, 06.61, "N"), GPSCoordinate(16, 40, 13.93, "E")),
                         (GPSCoordinate(49, 20, 44.53, "N"), GPSCoordinate(16, 39, 0.29, "E"))]),
        FishingLocation("463064", "SVITAVA 3", "BLANSKO", 12.5,
                        [(GPSCoordinate(49, 20, 44.53, "N"), GPSCoordinate(16, 39, 0.29, "E")),
                         (GPSCoordinate(49, 26, 27.04, "N"), GPSCoordinate(16, 37, 21.57, "E"))]),
        FishingLocation("463065", "SVITAVA 4", "BOSKOVICE", 13.0,
                        [(GPSCoordinate(49, 26, 27.04, "N"), GPSCoordinate(16, 37, 21.57, "E")),
                         (GPSCoordinate(49, 31, 21.98, "N"), GPSCoordinate(16, 35, 5.25, "E"))]),
        FishingLocation("463066", "SVITAVA 5", "LETOVICE", 11.3,
                        [(GPSCoordinate(49, 31, 21.98, "N"), GPSCoordinate(16, 35, 5.25, "E")),
                         (GPSCoordinate(49, 35, 21.83, "N"), GPSCoordinate(16, 32, 25.98, "E")),
                         (GPSCoordinate(49, 32, 39.38, "N"), GPSCoordinate(16, 34, 24.39, "E")),
                         (GPSCoordinate(49, 33, 15.15, "N"), GPSCoordinate(16, 33, 25.41, "E"))]),
        FishingLocation("463067", "SVRATKA 7-8", "TIŠNOV", 40.0,
                        [(GPSCoordinate(49, 19, 32.60, "N"), GPSCoordinate(16, 25, 33.76, "E")),
                         (GPSCoordinate(49, 27, 26.42, "N"), GPSCoordinate(16, 20, 12.47, "E"))]),
        FishingLocation("463068", "SVRATKA 9-10", "NEDVĚDICE", 24.0,
                        [(GPSCoordinate(49, 27, 26.42, "N"), GPSCoordinate(16, 20, 12.47, "E")),
                         (GPSCoordinate(49, 32, 51.52, "N"), GPSCoordinate(16, 20, 20.74, "E"))]),
        FishingLocation("463069", "SVRATKA 11P", "VÍR", 16.0,
                        [(GPSCoordinate(49, 32, 51.52, "N"), GPSCoordinate(16, 20, 20.74, "E")),
                         (GPSCoordinate(49, 33, 51.82, "N"), GPSCoordinate(16, 18, 35.50, "E"))]),
        FishingLocation("463070", "SVRATKA 12", "JIMRAMOV", 11.2,
                        [(GPSCoordinate(49, 35, 38.753, "N"), GPSCoordinate(16, 14, 39.169, "E")),
                         (GPSCoordinate(49, 39, 36.55, "N"), GPSCoordinate(16, 13, 16.81, "E"))]),
        FishingLocation("463071", "SVRATKA 14", "SVRATKA", 9.5,
                        [(GPSCoordinate(49, 41, 28.59, "N"), GPSCoordinate(16, 8, 23.72, "E")),
                         (GPSCoordinate(49, 41, 22.16, "N"), GPSCoordinate(15, 59, 32.92, "E")),
                         (GPSCoordinate(49, 42, 24.19, "N"), GPSCoordinate(16, 1, 28.66, "E"))]),
        FishingLocation("463073", "TRESNÝ POTOK", "OLEŠNICE NA MORAVĚ", 2.0, []),
        FishingLocation("463074", "TUPESKÝ POTOK 1", "UHERSKÉ HRADIŠTĚ", 1.0, []),
        FishingLocation("463075", "ÚMOŘÍ 1", "BOSKOVICE", 3.5,
                        [(GPSCoordinate(49, 28, 41.40, "N"), GPSCoordinate(16, 36, 49.58, "E")),
                         (GPSCoordinate(49, 30, 38.11, "N"), GPSCoordinate(16, 29, 52.74, "E"))]),
        FishingLocation("463076", "VALOVÁ - ROMŽE 3", "KONICE", 4.0,
                        [(GPSCoordinate(49, 30, 48.68, "N"), GPSCoordinate(17, 2, 18.63, "E")),
                         (GPSCoordinate(49, 35, 15.09, "N"), GPSCoordinate(16, 53, 29.67, "E"))]),
        FishingLocation("463078", "VLÁRA 2", "SLAVIČÍN", 6.0,
                        [(GPSCoordinate(49, 6, 00.37, "N"), GPSCoordinate(17, 55, 58.38, "E")),
                         (GPSCoordinate(49, 12, 41.21, "N"), GPSCoordinate(17, 58, 20.79, "E")),
                         (GPSCoordinate(49, 4, 20.17, "N"), GPSCoordinate(17, 56, 52.47, "E")),
                         (GPSCoordinate(49, 1, 15.13, "N"), GPSCoordinate(17, 55, 6.58, "E")),
                         (GPSCoordinate(49, 5, 22.64, "N"), GPSCoordinate(17, 52, 19.41, "E")),
                         (GPSCoordinate(49, 7, 54.88, "N"), GPSCoordinate(17, 51, 34.90, "E")),
                         (GPSCoordinate(49, 4, 27.96, "N"), GPSCoordinate(17, 58, 47.71, "E")),
                         (GPSCoordinate(49, 1, 33.38, "N"), GPSCoordinate(17, 58, 50.42, "E")),
                         (GPSCoordinate(49, 5, 47.39, "N"), GPSCoordinate(17, 50, 45.45, "E")),
                         (GPSCoordinate(49, 7, 47.24, "N"), GPSCoordinate(17, 50, 08.19, "E")),
                         (GPSCoordinate(49, 2, 46.97, "N"), GPSCoordinate(18, 1, 54.23, "E")),
                         (GPSCoordinate(49, 1, 23.29, "N"), GPSCoordinate(18, 0, 24.63, "E"))]),
        FishingLocation("463080", "VRBKA 1", "UHERSKÉ HRADIŠTĚ", 1.2, []),
    ]
