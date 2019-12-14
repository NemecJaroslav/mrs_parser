from unittest import TestCase
from production_code.mrs_parser import MRSParser, GPSCoordinate
from .test_data import (get_expected_locations, get_expected_location_ids,
                        get_expected_location_names, get_expected_gps)


class TestMRSParser(TestCase):
    def setUp(self):
        self.parser = MRSParser()

    def test_get_locations(self):
        expected_locations = get_expected_locations()
        self.assertEqual(245, len(expected_locations))
        self.assertEqual(sorted(expected_locations),
                         sorted(set(expected_locations)))
        self.assertEqual(sorted(expected_locations),
                         sorted(self.parser._get_locations()))

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

    def test_get_headquarters(self):
        expected_results = [
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/176-bacicky-potok",
                "Hrotovice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/177-balas-1a",
                "Zlín"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/178-balinka-1",
                "Velké Meziříčí"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/179-balinka-1a",
                "Velké Meziříčí"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/180-balinka-1b",
                "Velké Meziříčí"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/181-bily-potok-2a",
                "Velká Bíteš"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/182-blata-3",
                "Prostějov"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/183-bobrava-1",
                "Brno 1"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/184-bobrava-2",
                "Rosice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/185-bobrava-2a",
                "Rosice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/186-brodecky-potok-1",
                "Němčice nad Hanou"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/187-brtnice-1",
                "Brtnice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/188-brtnice-1a",
                "Brtnice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/189-buchlovicky-potok-1",
                "Nedakonice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/190-buchlovicky-potok-1m",
                "Nedakonice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/191-bystrice-pernstejnska-2",
                "Bystřice nad Pernštejnem"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/777-bykovka-1a",
                "Blansko"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/192-cezava-1",
                "Brno 5"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/193-cezava-1a",
                "Brno 5"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/194-cezava-2",
                "Slavkov"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/195-cezava-2a",
                "Slavkov"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/196-cezava-3a",
                "Slavkov"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/197-cikhajsky-potok-1",
                "Žďár nad Sázavou"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/198-drevnice-1",
                "Zlín"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/199-drevnice-1a",
                "Zlín"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/200-dyje-2",
                "Břeclav"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/201-dyje-3",
                "Břeclav"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/202-dyje-3a",
                "Břeclav"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/203-dyje-4",
                "Podivín"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/204-dyje-4a",
                "Podivín"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/205-dyje-4b",
                "Rakvice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/206-dyje-4c",
                "Rakvice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/207-dyje-4c-1",
                "Brno 5"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/209-dyje-4d",
                "Lednice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/210-dyje-4e",
                "Zaječí"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/211-dyje-4g",
                "Zaječí"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/212-dyje-4m",
                "Podivín"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/128-dyje-5",
                "MRS, z.s. Brno"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/213-dyje-5a",
                "Hustopeče"
            ],
            # TODO: dropped " a pobočný spolek Mikulov" from expected result
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/130-dyje-7",
                "MRS, z.s. Brno"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/214-dyje-7a",
                "Mikulov"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/216-dyje-7b",
                "Mikulov"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/215-dyje-8",
                "Hrušovany nad Jevišovkou"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/217-dyje-9",
                "Znojmo"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/218-dyje-10",
                "Znojmo"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/219-dyje-11",
                "Znojmo"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/220-dyje-11a",
                "Znojmo"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/221-dyje-15",
                "Znojmo"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/222-dyje-19",
                "Telč"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/223-dyje-19a",
                "Telč"
            ],

            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/224-dyje-19b",
                "Telč"
            ],

            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/225-dyje-19c",
                "Telč"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/226-greslovomytsky-potok-1",
                "Moravské Budějovice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/614-habrovansky-potok-1a",
                "Rajhrad"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/227-hana-1",
                "Němčice nad Hanou"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/228-hana-1a",
                "Němčice nad Hanou"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/232-hana-1b",
                "Němčice nad Hanou"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/229-hana-2",
                "Vyškov"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/230-hana-3",
                "Vyškov"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/231-hana-3m",
                "Vyškov"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/234-herdy",
                "Lednice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/233-hloucela-1",
                "Prostějov"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/292-mala-becva-1",
                "Chropyně"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/293-mala-becva-1a",
                "Chropyně"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/294-markovka-1",
                "Třebíč"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/295-mocla-1",
                "Hrotovice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/296-mocla-1m",
                "Hrotovice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/297-mocla-2",
                "Hrotovice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/298-morava-2",
                "Lanžhot"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/299-morava-3",
                "Tvrdonice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/300-morava-4",
                "Hodonín"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/301-morava-4a",
                "Hodonín"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/302-morava-4b",
                "Dubňany"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/303-morava-4c",
                "Ratíškovice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/304-morava-5",
                "Hodonín"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/305-morava-6",
                "Strážnice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/306-morava-6a",
                "Strážnice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/307-morava-6m",
                "Strážnice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/308-morava-7",
                "Veselí nad Moravou"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/309-morava-7a",
                "Veselí nad Moravou"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/310-morava-8",
                "Uherský Ostroh"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/311-morava-8a",
                "Uherský Ostroh"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/312-morava-9",
                "Staré Město"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/313-morava-9a",
                "Staré Město"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/314-morava-9b",
                "Kostelany nad Moravou"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/315-morava-9c",
                "Staré Město"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/316-morava-10",
                "Uherské Hradiště"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/317-morava-10a",
                "Uherské Hradiště"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/318-morava-11",
                "Uherské Hradiště"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/319-morava-12",
                "Otrokovice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/320-morava-12a",
                "Otrokovice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/324-morava-12m",
                "Otrokovice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/321-morava-13",
                "Kroměříž"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/322-morava-13a",
                "Kroměříž"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/325-morava-13b",
                "Kroměříž"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/323-morava-13c",
                "Kvasice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/326-mysluvka-1",
                "Mrákotín"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/327-mysluvka-1m",
                "Mrákotín"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/328-navesni-rybnik",
                "Blansko"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/329-okluka-1",
                "Hluk"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/330-olesnicky-potok-1a",
                "Olešnice na Moravě"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/331-olsava-1",
                "Kunovice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/332-olsava-1a",
                "Kunovice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/333-olsava-1b",
                "Kunovice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/334-olsava-2",
                "Uherský Brod"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/335-olsava-2a",
                "Uherský Brod"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/336-olsava-3a",
                "Bojkovice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/337-oslava-1",
                "Oslavany"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/338-oslava-1m",
                "Ivančice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/339-oslava-2",
                "Náměšť nad Oslavou"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/340-oslava-3",
                "Náměšť nad Oslavou"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/341-oslava-4",
                "Náměšť nad Oslavou"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/342-oslava-4m",
                "Náměšť nad Oslavou"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/343-oslava-5",
                "Velké Meziříčí"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/344-oslava-6a",
                "Velké Meziříčí"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/345-oslava-7",
                "Velké Meziříčí"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/346-oslava-7a",
                "Velké Meziříčí"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/347-oslava-8",
                "Žďár nad Sázavou"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/348-pavov-1",
                "Jihlava"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/349-podomsky-potok-1",
                "Blansko"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/350-podomsky-potok-1a",
                "Blansko"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/351-podomsky-potok-1b",
                "Blansko"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/352-prusanecky-potok-1",
                "Velké Bílovice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/237-chlumsky-potok-1a",
                "Zlín"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/238-ivanovicky-potok-1",
                "Brno 4"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/239-janustice-1a",
                "Zlín"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/240-jaromerice-1",
                "Moravské Budějovice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/241-jaromerice-1a",
                "Moravské Budějovice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/783-jaromerice-1b",
                "Moravské Budějovice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/242-jaromerice-1m",
                "Moravské Budějovice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/243-jevisovka-1",
                "Hrušovany nad Jevišovkou"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/244-jevisovka-1a",
                "Hrušovany nad Jevišovkou"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/245-jevisovka-2",
                "Jevišovice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/246-jevisovka-2a",
                "Jevišovice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/247-jevisovka-3",
                "Jevišovice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/248-jihlava-1",
                "Pohořelice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/249-jihlava-1m",
                "Pohořelice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/250-jihlava-2",
                "Pohořelice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/251-jihlava-3",
                "Dolní Kounice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/252-jihlava-4",
                "Ivančice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/785-jihlava-4a",
                "Ivančice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/253-jihlava-5m",
                "Nová Ves"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/254-jihlava-6",
                "Mohelno"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/267-jihlava-6a",
                "Mohelno"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/255-jihlava-7-8",
                "Třebíč"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/256-jihlava-9",
                "Třebíč"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/257-jihlava-10",
                "Třebíč"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/258-jihlava-11",
                "Třebíč"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/259-jihlava-12",
                "Jihlava"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/260-jihlava-13",
                "Jihlava"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/261-jihlava-13a",
                "Jihlava"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/266-jihlava-13b",
                "Jihlava"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/262-jihlava-13c",
                "Jihlava"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/263-jihlava-14",
                "Jihlava"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/264-jihlava-15",
                "Batelov"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/265-jihlava-15a",
                "Batelov"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/268-klimsak-1",
                "Rájec - Jestřebí"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/269-klimsak-1m",
                "Rájec - Jestřebí"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/270-kockuv-rybnik-1",
                "Boskovice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/271-kovalovicky-potok-1",
                "Kovalovice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/272-kretinka-1",
                "Letovice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/273-krovacka-1",
                "Slavkov"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/274-kyjovka-2",
                "Lanžhot"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/275-kyjovka-2-1",
                "Kostice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/276-kyjovka-2-2",
                "Týnec"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/277-kyjovka-2a",
                "Lanžhot"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/278-kyjovka-2b",
                "Hodonín"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/279-kyjovka-2c",
                "Kostice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/280-kyjovka-2c-1",
                "Lanžhot"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/281-kyjovka-2d",
                "Tvrdonice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/282-kyjovka-2e",
                "Týnec"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/283-kyjovka-3",
                "Kyjov"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/284-kyjovka-3a",
                "Kyjov"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/285-kyjovka-3b",
                "Ždánice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/286-kyjovka-3c",
                "Kyjov"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/287-kyjovka-4a",
                "Osvětimany"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/288-lisenska-ricka-1",
                "Brno 4"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/289-loucka-1a",
                "Dolní Loučky"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/290-loucka-4a",
                "Nové Město na Moravě"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/291-lubi-1",
                "Třebíč"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/354-rakovec-1",
                "Slavkov"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/355-rakovec-2",
                "Vyškov"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/356-roketnice-1",
                "Šlapanice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/357-rokytna-1",
                "Moravský Krumlov"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/358-rokytna-1m",
                "Moravský Krumlov"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/359-rokytna-2",
                "Moravský Krumlov"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/360-rokytna-3",
                "Rouchovany"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/361-rokytna-3a",
                "Rouchovany"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/362-rokytna-4",
                "Jaroměřice nad Rokytnou"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/363-rokytna-5",
                "Jaroměřice nad Rokytnou"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/365-rokytna-5m",
                "Jaroměřice nad Rokytnou"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/364-rokytna-6",
                "Třebíč"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/769-rokytna-6a",
                "Jaroměřice nad Rokytnou"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/366-romze-3a",
                "Konice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/367-romze-3c",
                "Konice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/368-romze-3d",
                "Konice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/369-rostenicky-potok-1",
                "Vyškov"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/370-rusava-2",
                "Holešov"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/371-rusava-2a",
                "Bystřice pod Hostýnem"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/372-rusava-2b",
                "Holešov"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/373-sazava-17",
                "Žďár nad Sázavou"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/374-sazava-18",
                "Žďár nad Sázavou"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/376-sazava-19",
                "Žďár nad Sázavou"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/377-starecsky-potok-1",
                "Třebíč"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/378-starecsky-potok-1a",
                "Rudíkov"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/379-starecsky-potok-1b",
                "Rudíkov"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/380-svitava-1",
                "Brno 3"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/382-svitava-3a",
                "Blansko"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/381-svitava-5a",
                "Letovice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/383-svratka-1",
                "Vranovice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/384-svratka-1a",
                "Vranovice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/385-svratka-1m",
                "Vranovice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/386-svratka-2",
                "Brno 5"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/395-svratka-2b",
                "Brno 5"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/387-svratka-3",
                "Brno 1"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/388-svratka-4",
                "Brno 2"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/389-svratka-5",
                "Brno 2"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/390-svratka-6",
                "Veverská Bitýška"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/391-svratka-7-8a",
                "Tišnov"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/392-svratka-11m",
                "Vír"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/393-svratka-14a",
                "Svratka"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/394-svratka-14m",
                "Svratka"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/396-scavnice-2a",
                "Sehradice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/397-svabovsky-potok-1",
                "Batelov"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/398-trkmanka-1",
                "Podivín"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/399-trkmanka-2",
                "Velké Bílovice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/400-trestsky-potok-1",
                "Třešť"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/401-valcha-1",
                "Třešť"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/402-valcha-2",
                "Třešť"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/403-valova-2",
                "Prostějov"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/779-vapovka-2",
                "Telč"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/404-velicka-1",
                "Strážnice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/405-velicka-1m",
                "Strážnice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/406-velicka-2",
                "Veselí nad Moravou"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/416-vicemilice-1",
                "Slavkov"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/407-vlara-1",
                "Slavičín"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/408-vlara-1a",
                "Slavičín"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/409-vracov-1",
                "Vracov"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/410-zdarna-1",
                "Boskovice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/411-zeletavka-1",
                "Police"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/412-zeletavka-1a",
                "Police"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/413-zeletavka-2",
                "Jemnice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/414-zeletavka-2a",
                "Jemnice"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/415-zeletavka-2b",
                "Želetava"
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/778-zeletavka-2c",
                "Jemnice"
            ],
        ]
        self.assertEqual(245, len(expected_results))
        locations = [expected_result[0] for expected_result in expected_results]
        self.assertEqual(sorted(locations),
                         sorted(set(locations)))
        for expected_result in expected_results:
            context = self.parser._get_decoded_source_page(expected_result[0])
            actual = self.parser._get_headquarters(context)
            self.assertEqual(expected_result[1], actual)
