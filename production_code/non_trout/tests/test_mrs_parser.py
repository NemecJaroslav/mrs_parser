from unittest import TestCase
from production_code.common.mrs_parser import GPSCoordinate
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
            # self.assertEqual(expected_fishing_location.gps_locations,
            #                  actual_fishing_location.gps_locations)

    # TODO: add more test cases & uniqueness test
    def test_convert_string_to_gps(self):
        expected_results = [
            [
                ["49°1'54.80''N, 15°33'59.90''E"],
                [
                    (GPSCoordinate(49, 1, 54.80, "N"),
                     GPSCoordinate(15, 33, 59.90, "E")),
                ],
            ],
            [
                ["49°08'53.56''N, 15°40'23.27''E",
                 "49°08'04.95''N, 15°39'38.83''E"
                 ],
                [
                    (GPSCoordinate(49, 8, 53.56, "N"),
                     GPSCoordinate(15, 40, 23.27, "E")),
                    (GPSCoordinate(49, 8, 04.95, "N"),
                     GPSCoordinate(15, 39, 38.83, "E"))
                ],
            ],
            [
                ["49°04'53.05''N, 15°35'06.67''E",
                 "49°04'42.46''N, 15°32'00.20''E",
                 "49°00'51.50''N, 15°34'48.08''E",
                 "49°00'53.76''N, 15°34'38.95''E",
                 "49°02'40.77''N, 15°33'54.81''E"
                 ],
                [
                    (GPSCoordinate(49, 4, 53.05, "N"),
                     GPSCoordinate(15, 35, 06.67, "E")),
                    (GPSCoordinate(49, 4, 42.46, "N"),
                     GPSCoordinate(15, 32, 00.20, "E")),
                    (GPSCoordinate(49, 0, 51.50, "N"),
                     GPSCoordinate(15, 34, 48.08, "E")),
                    (GPSCoordinate(49, 0, 53.76, "N"),
                     GPSCoordinate(15, 34, 38.95, "E")),
                    (GPSCoordinate(49, 2, 40.77, "N"),
                     GPSCoordinate(15, 33, 54.81, "E"))
                ]
            ]
        ]
        for expected_result in expected_results:
            self.assertEqual(expected_result[1],
                             self.parser._convert_string_to_gps(expected_result[0]))
