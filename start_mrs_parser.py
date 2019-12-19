from production_code.mrs_parser import MRSParser

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
    # parser.print_all_headquarters_and_their_locations()
    # parser.print_all_headquarters_and_their_areas()
    parser.print_suitable_fishing_locations(
        (49.4677572, 17.2850111),
        (0., 30.))
