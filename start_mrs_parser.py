from production_code.mrs_parser import MRSParser
from production_code.distance_limit import DistanceLimit

# Marek
# 49.1686025, 16.5705978
# Ja
# 49.1806731, 16.6801281
# Verovany
# 49.4677572, 17.2850111
# Kamechy
# 49.2185178, 16.5091428

if __name__ == "__main__":
    parser = MRSParser()
    parser.parse()
    parser.print_all_headquarters_and_their_locations()
    parser.print_all_headquarters_and_their_areas()
    parser.print_suitable_fishing_locations(
        (49.1806731, 16.6801281),
        DistanceLimit(0., 30.))
    parser.print_fishing_summary([
        "461171",
        "461221",
        "461187",
        "461041",
        "461229",
        "461187",
        "461015",
        "461015",
        "461041",
        "461119",
        "461187",
        "461119",
        "461119",
        "461041",
        "461015",
        "461003",
        "461119",
        "461015",
        "461119",
        "461015",
        "461015",
        "461041",
        "461041",
        "461041",
        "461134",
        "461101",
        "461187",
        "461127",
        "461119",
        "461012",
        "461134",
        "461041",
        "461012",
        "461012",
        "461213",
        "461015",
    ])
