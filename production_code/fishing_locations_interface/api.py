__all__ = [
    "get_available_organisations",
    "get_suitable_fishing_locations",
    "get_all_headquarters",
    "get_total_area_for_given_headquarter",
    "get_fishing_locations_for_given_headquarter",
    "prepare_parser",
]

from .fishing_locations_interface import (
    get_available_organisations, get_suitable_fishing_locations, get_all_headquarters,
    get_total_area_for_given_headquarter, get_fishing_locations_for_given_headquarter, prepare_parser)
