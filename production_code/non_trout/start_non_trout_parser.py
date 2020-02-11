from production_code.common.distance_limit import DistanceLimit
from production_code.non_trout.non_trout_parser import NonTroutParser

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
    parser = NonTroutParser()
    parser.parse()
    # parser.print_all_headquarters_and_their_locations()
    # parser.print_all_headquarters_and_their_areas()
    parser.print_suitable_fishing_locations(
        (49.4677572, 17.2850111),
        DistanceLimit(0., 30.))
    # parser.print_fishing_summary_given_by_id([
    #     "461171",
    #     "461221",
    #     "461187",
    #     "461041",
    #     "461229",
    #     "461187",
    #     "461015",
    #     "461015",
    #     "461041",
    #     "461119",
    #     "461187",
    #     "461119",
    #     "461119",
    #     "461041",
    #     "461015",
    #     "461003",
    #     "461119",
    #     "461015",
    #     "461119",
    #     "461015",
    #     "461015",
    #     "461041",
    #     "461041",
    #     "461041",
    #     "461134",
    #     "461101",
    #     "461187",
    #     "461127",
    #     "461119",
    #     "461012",
    #     "461134",
    #     "461041",
    #     "461012",
    #     "461012",
    #     "461213",
    #     "461015",
    # ])
    #
    # parser.print_fishing_summary_given_by_name([
    #     "Žďárná 1",
    #     "Kovalovický potok 1",
    #     "Žďárná 1",
    # ])

    parser.print_suspiciously_close_gps_locations(DistanceLimit(0.0, 0.5))
