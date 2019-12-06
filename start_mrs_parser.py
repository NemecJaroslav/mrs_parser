from mrs_parser import MRSParser

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
    result = parser.get_suitable_fishing_locations(
        (49.1806731, 16.6801281),
        (0., 30.))
    for _ in result:
        print(_)
