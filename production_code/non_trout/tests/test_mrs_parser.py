from unittest import TestCase
from production_code.non_trout.non_trout_parser import NonTroutParser
from production_code.non_trout.tests.test_data import get_expected_fishing_locations


class TestMRSParser(TestCase):
    def setUp(self):
        self.parser = NonTroutParser()
        self.parser.parse()

    def test_parse(self):
        expected_fishing_locations = get_expected_fishing_locations()
        actual_fishing_locations = self.parser._fishing_locations

        expected_fishing_locations.sort(key=lambda x: x.identifier)
        actual_fishing_locations.sort(key=lambda x: x.identifier)

        self.assertEqual(len(expected_fishing_locations),
                         len(actual_fishing_locations))
        for (expected_fishing_location,
             actual_fishing_location) in zip(expected_fishing_locations,
                                             actual_fishing_locations):
            self.assertEqual(expected_fishing_location.identifier,
                             actual_fishing_location.identifier)
            self.assertEqual(expected_fishing_location.name,
                             actual_fishing_location.name)
            self.assertEqual(expected_fishing_location.headquarter,
                             actual_fishing_location.headquarter)
            self.assertEqual(expected_fishing_location.area,
                             actual_fishing_location.area)
            self.assertEqual(expected_fishing_location.gps_locations,
                             actual_fishing_location.gps_locations)
