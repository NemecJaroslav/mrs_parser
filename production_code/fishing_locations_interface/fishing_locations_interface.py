from production_code.CRS.NorthMoraviaAndSilesia.salmonid.parser import NorthMoraviaAndSilesiaSalmonidParser
from production_code.CRS.NorthMoraviaAndSilesia.non_salmonid.parser import NorthMoraviaAndSilesiaNonSalmonidParser
from production_code.MRS.salmonid.salmonid_parser import SalmonidParser
from production_code.MRS.non_salmonid.non_salmonid_parser import NonSalmonidParser


parsers = [
    NonSalmonidParser(),
    NorthMoraviaAndSilesiaNonSalmonidParser(),
    SalmonidParser(),
    NorthMoraviaAndSilesiaSalmonidParser(),
]


def prepare_parser(parser_identifier):
    parsers[parser_identifier].parse()


def get_available_organisations():
    return [parser.get_parser_description() for parser in parsers]


def get_suitable_fishing_locations(parser_identifier, start_point, distance_limit):
    return parsers[parser_identifier].get_suitable_fishing_locations(start_point, distance_limit)
