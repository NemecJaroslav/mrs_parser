from unittest import TestCase
from production_code.mrs_parser import MRSParser, GPSCoordinate
from .test_data import (get_expected_locations_url, get_expected_location_ids,
                        get_expected_location_names, get_expected_gps,
                        get_expected_headquarters, get_expected_area)


class TestMRSParser(TestCase):
    def setUp(self):
        self.parser = MRSParser()

    def test_get_locations_url(self):
        expected_locations_url = get_expected_locations_url()
        self.assertEqual(245, len(expected_locations_url))
        self.assertEqual(sorted(expected_locations_url),
                         sorted(set(expected_locations_url)))
        self.assertEqual(sorted(expected_locations_url),
                         sorted(self.parser._get_locations_url()))

    def test_get_location_id(self):
        expected_results = get_expected_location_ids()
        self.assertEqual(245, len(expected_results))
        locations = [expected_result[0] for expected_result in expected_results]
        ids = [expected_result[1] for expected_result in expected_results]
        self.assertEqual(sorted(locations),
                         sorted(set(locations)))
        self.assertEqual(sorted(ids),
                         sorted(set(ids)))
        for expected_result in expected_results:
            context = self.parser._get_decoded_source_page(expected_result[0])
            actual = self.parser._get_location_id(context)
            self.assertEqual(expected_result[1], actual)

    def test_get_location_name(self):
        expected_results = get_expected_location_names()
        self.assertEqual(245, len(expected_results))
        locations = [expected_result[0] for expected_result in expected_results]
        names = [expected_result[1] for expected_result in expected_results]
        self.assertEqual(sorted(locations),
                         sorted(set(locations)))
        self.assertEqual(sorted(names),
                         sorted(set(names)))
        for expected_result in expected_results:
            context = self.parser._get_decoded_source_page(expected_result[0])
            actual = self.parser._get_location_name(context)
            self.assertEqual(expected_result[1], actual)

    def test_get_gps(self):
        expected_results = get_expected_gps()
        self.assertEqual(245, len(expected_results))
        locations = [expected_result[0] for expected_result in expected_results]
        self.assertEqual(sorted(locations),
                         sorted(set(locations)))
        for expected_result in expected_results:
            context = self.parser._get_decoded_source_page(expected_result[0])
            actual = self.parser._get_gps(context)
            self.assertEqual(sorted(expected_result[1]),
                             sorted(actual))

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

    def test_get_headquarter(self):
        expected_results = get_expected_headquarters()
        self.assertEqual(245, len(expected_results))
        locations = [expected_result[0] for expected_result in expected_results]
        self.assertEqual(sorted(locations),
                         sorted(set(locations)))
        for expected_result in expected_results:
            context = self.parser._get_decoded_source_page(expected_result[0])
            actual = self.parser._get_headquarter(context)
            self.assertEqual(expected_result[1], actual)

    def test_get_area(self):
        expected_results = get_expected_area()
        self.assertEqual(245, len(expected_results))
        locations = [expected_result[0] for expected_result in expected_results]
        self.assertEqual(sorted(locations),
                         sorted(set(locations)))
        for expected_result in expected_results:
            context = self.parser._get_decoded_source_page(expected_result[0])
            actual = self.parser._get_area(context)
            self.assertEqual(expected_result[1], actual)

