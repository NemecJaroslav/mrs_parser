from production_code.common.distance_limit import DistanceLimit
from production_code.CRS.NorthMoraviaAndSilesia.salmonid.parser import NorthMoraviaAndSilesiaSalmonidParser

# Marek
# 49.1686025, 16.5705978
# Ja
# 49.1806731, 16.6801281
# Verovany
# 49.4677572, 17.2850111
# Kamechy
# 49.2185178, 16.5091428
# Protivanov
# 49.4823661, 16.8364286

if __name__ == "__main__":
    parser = NorthMoraviaAndSilesiaSalmonidParser()
    parser.parse()

    parser.print_all_headquarters_and_their_locations()
    parser.print_suitable_fishing_locations((49.1806731, 16.6801281), DistanceLimit(0., 3000.))
    parser.print_all_headquarters_and_their_areas()
    parser.print_suspiciously_close_gps_locations(DistanceLimit(0.0, 0.5))
    parser.print_all_headquarters_and_distance_to_their_locations()
    parser.print_fishing_summary_given_by_id(["473024", "473029"])
    parser.print_fishing_summary_given_by_name(["DESNÁ 3", "BYSTŘICE HANÁCKÁ 2 P"])
