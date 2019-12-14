from unittest import TestCase
from production_code.mrs_parser import MRSParser, GPSCoordinate
from .test_data import (get_expected_locations, get_expected_location_ids,
                        get_expected_location_names)


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
        expected_results = [
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/176-bacicky-potok",
                ["49°05'24.06''N, 15°59'59.60''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/177-balas-1a",
                ["49°11'56.49''N, 17°36'03.18''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/178-balinka-1",
                ["49°21'07.60''N, 16°00'58.25''E",
                 "49°23'36.27''N, 15°52'27.94''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/179-balinka-1a",
                ["49°23'42.75''N, 15°52'12.96''E",
                 "49°24'19.00''N, 15°50'37.48''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/180-balinka-1b",
                ["49°23'09.95''N, 15°54'35.64''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/181-bily-potok-2a",
                ["49°18'17.71''N, 16°12'42.14''E", "49°17'28.09''N, 16°14'28.86''E"]
            ],
            [
                 "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/182-blata-3",
                 ["49°29'07.33''N, 17°13'28.88''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/183-bobrava-1",
                ["49°06'31.40''N, 16°37'35.75''E",
                 "49°08'17.26\"N, 16°28'27.78\"E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/184-bobrava-2",
                ["49°08'17.26\"N, 16°28'27.78\"E",
                 "49°14'57.64\"N, 16°18'45.80\"E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/185-bobrava-2a",
                ["49°10'22.83''N, 16°25'16.66''E",
                 "49°14'8.32\"N, 16°15'56.56\"E",
                 "49°11'13.12''N, 16°22'3.87''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/186-brodecky-potok-1",
                ["49°20'05.80''N, 17°11'44.88''E",
                 "49°23'18.60''N, 17°03'26.21\"E",
                 "49°20'14.18''N, 17°12'17.33''E",
                 "49°20'26.52''N, 17°10'53.40''E",
                 "49°22'1.52''N, 17°7'26.38''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/187-brtnice-1",
                ["49°20'09.62''N, 15°44'32.61''E",
                 "49°15'18.32''N, 15°39'41.10''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/188-brtnice-1a",
                ["49°17'18.77''N, 15°40'40.93''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/189-buchlovicky-potok-1",
                ["49°01'04.97''N, 17°23'21.02''E",
                 "49°04'37.71''N, 17°19'32.02''E",
                 "49°04'37.90''N, 17°19'32.18''E",
                 "49°01'09.57''N, 17°23'03.33''E",
                 "49°01'04.97''N, 17°23'21.02''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/190-buchlovicky-potok-1m",
                ["49°01'33.01\"N, 17°22'59.22''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/191-bystrice-pernstejnska-2",
                ["49°33'43.25''N, 16°11'07.02''E", "49°33'09.18''N, 16°11'44.72''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/777-bykovka-1a",
                ["49°25'2.62''N, 16°34'35.40''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/192-cezava-1",
                ["49°02'26.10''N, 16°36'55.23''E",
                 "49°06'17.88''N, 16°45'54.61''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/193-cezava-1a",
                ["49°04'16.30''N, 16°38'13.96''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/194-cezava-2",
                ["49°06'17.88''N, 16°45'54.61''E",
                 "49°09'26.75''N, 17°16'55.45''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/195-cezava-2a",
                ["49°08'51.74''N, 16°53'01.36''E",
                 "49°8'44.42''N, 16°53'25.31''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/196-cezava-3a",
                ["49°08'33.20''N, 17°00'25.87''E",
                 "49°08'32.51''N, 17°00'23.18''E",
                 "49°8'7.22''N, 16°54'38.08''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/197-cikhajsky-potok-1",
                ["49°35'17.85''N 15°56'43.63''E",
                 "49°37'6.38''N, 15°57'11.29''E",
                 "49°36'25.71''N, 15°57'09.15''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/198-drevnice-1",
                ["49°12'13.70''N, 17°30'40.70''E",
                 "49°13'16.32''N, 17°42'53.99''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/199-drevnice-1a",
                ["49°12'34.82''N, 17°33'18.67''E",
                 "49°13'21.62''N, 17°40'16.96''E",
                 "49°09'49.94''N, 17°42'26.44''E",
                 "49°13'48.63''N, 17°38'09.51''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/200-dyje-2",
                ["48°41'30.09''N, 16°54'59.92''E",
                 "48°42'59.78''N, 16°53'15.84''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/201-dyje-3",
                ["48°42'59.78''N, 16°53'15.84''E",
                 "48°48'13.91''N, 16°51'13.87''E",
                 "48°46'44.31''N, 16°53'06.81''E",
                 "48°49'26.66''N, 16°50'49.89''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/202-dyje-3a",
                ["48°45'33.04''N, 16°52'11.83''E",
                 "48°45'36.94''N, 16°52'07.37''E",
                 "48°45.569' N  16°52.717' E",
                 "48°46.974' N  16°54.025' E",
                 "48°48'04.92''N, 16°52'24.92''E",
                 "48°47'35.73''N, 16°52'11.48''E",
                 "48°48'20.39''N, 16°51'05.75''E",
                 "48°43'31.24''N, 16°53'24.55''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/203-dyje-4",
                ["48°48'13.91''N, 16°51'13.87''E",
                 "48°49'4.79''N, 16°48'28.68''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/204-dyje-4a",
                ["48°50'09.51''N, 16°50'10.43''E",
                 "48°48'21.45''N, 16°50'23.16''E",
                 "48°48'41.70''N, 16°49'0.81''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/205-dyje-4b",
                ["48°49'37.90''N, 16°46'11.79''E",
                 "48°51'29.69''N, 16°43'20.09''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/206-dyje-4c",
                ["48°50'52.304\"N, 16°44'04.855\"E",
                 "48°51'01.19''N, 16°43'54.54''E",
                 "48°49'42.33''N, 16°46'15.81''E",
                 "48°49'28.37''N, 16°45'51.86''E",
                 "48°50'8.16''N, 16°45'26.30''E",
                 "48°50'03.03''N, 16°46'15.00''E",
                 "48°51'1.99''N, 16°47'17.05''E",
                 "48°49'52.09''N, 16°46'59.65''E",
                 "48°51'04.61''N, 16°49'35.74''E",
                 "48°50'49.38''N, 16°48'34.14''E",
                 "48°50'33.78''N, 16°48'57.57''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/207-dyje-4c-1",
                ["48°51'13.27''N, 16°44'01.34''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/209-dyje-4d",
                ["48°49'04.90''N, 16°48'28.06''E",
                 "48°49'37.75''N, 16°46'11.49''E",
                 "48°48'41.36''N, 16°49'00.52''E",
                 "48°48'35.57''N, 16°49'22.97''E",
                 "48°49'34.80''N, 16°47'19.15''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/210-dyje-4e",
                ["48°51'02.052\"N, 16°44'29.512\"E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/211-dyje-4g",
                ["48°51'01.081\"N, 16°44'39.372\"E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/212-dyje-4m",
                ["48°48'20.19''N, 16°51'05.87''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/128-dyje-5",
                ["48°51'30.47''N, 16°43'19.92''E",
                 "48°53'34.79''N, 16°38'39.31''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/213-dyje-5a",
                ["48°57'54.02''N, 16°44'07.12''E",
                 "48°57'46.65''N, 16°44'04.54''E",
                 "48°57'22.70''N, 16°42'34.50''E",
                 "49°00'50.21''N, 16°45'25.91''E",
                 "48°58'23.12''N, 16°48'18.08''E",
                 "48°54'11.74''N, 16°39'56.23''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/130-dyje-7",
                ["48°53'11.82''N, 16°35'38.98''E",
                 "48°48'24.71''N, 16°28'5.39''E",
                 "48°52'18\"N, 16°30'23.7\"E"
                 ]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/214-dyje-7a",
                ["48°53'17.10''N, 16°37'40.58''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/216-dyje-7b",
                ["48°53'48.22''N, 16°34'02.91''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/215-dyje-8",
                ["48°48'16.57''N, 16°27'41.90''E",
                 "48°44'17.46''N, 16°21'26.26''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/217-dyje-9",
                ["48°44'03.41''N, 16°20'13.71''E",
                 "48°46'08.23''N, 16°15'31.88''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/218-dyje-10",
                ["48°46'08.23''N, 16°15'31.68''E",
                 "48°48'48.60''N, 16°10'06.46''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/219-dyje-11",
                ["48°48'48.60''N, 16°10'06.46''E",
                 "48°51'16.64''N, 16°02'22.00''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/220-dyje-11a",
                ["48°53'00.05''N, 16°02'47.22''E",
                 "48°53'18.53''N, 16°3'6.16''E",
                 "48°52'18.89''N, 16°1'54.79''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/221-dyje-15",
                ["48°54'24.35''N, 15°49'10.55''E",
                 "48°53'13.45''N, 15°38'09.10''E",
                 "48°56'20.13''N, 15°42'08.35''E",
                 "48°57'42.53''N, 15°41'06.21''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/222-dyje-19",
                ["49°06'24.71''N, 15°26'45.12''E",
                 "49°09'38.64''N, 15°28'26.31''E",
                 "49°09'38.64''N, 15°28'26.31''E",
                 "49°09'49.69''N,15°28'15.06''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/223-dyje-19a",
                ["49°12'15.36''N, 15°30'31.14''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/224-dyje-19b",
                ["49°07'42.58''N, 15°27'19.97''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/225-dyje-19c",
                ["49°08'39.76\"N, 15°33'58.82\"E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/226-greslovomytsky-potok-1",
                ["48°58'48.41''N, 15°55'24.69''E",
                 "49°3'50.70''N, 15°42'3.94''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/614-habrovansky-potok-1a",
                ["49°13'32.17\"N, 16°52'54.464\"E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/227-hana-1",
                ["49°19'37.38''N, 17°21'50.76''E",
                 "49°19'50.66''N, 17°09'36.32''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/228-hana-1a",
                ["49°16'38.55''N, 17°14'41.95''E",
                 "49°14'02.27''N, 17°13'43.50''E",
                 "49°14'42.25''N, 17°12'32.96''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/232-hana-1b",
                ["49°18'21.143''N, 17°9'10.636''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/229-hana-2",
                ["49°19'50.86''N, 17°09'36.32''E",
                 "49°16'55.71''N, 16°59'42.35''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/230-hana-3",
                ["49°16'07.52''N, 17°08'38.14''E",
                 "49°19'08.18''N, 17°07'09.21''E",
                 "49°19'29.86''N, 17°01'15.55''E",
                 "49°19'27.13''N, 17°00'30.26''E",
                 "49°17'15.91\"N, 17°02'37.19\"E",
                 "49°15'05.96''N, 17°05'35.12''E",
                 "49°19'02.34\"N, 17°00'18.19\"E",
                 "49°20'26.61\"N, 17°04'24.07\"E",
                 "49°18'03.74''N, 17°06'29.50''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/231-hana-3m",
                ["49°16'09.30''N, 17°07'01.14''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/234-herdy",
                ["48°49'29.96\"N, 16°47'14.13\"E",
                 "48°49'22.84\"N, 16°47'07.95\"E",
                 "48°49'24.07\"N, 16°47'13.05\"E",
                 "48°49'25.23\"N, 16°47'19.69\"E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/233-hloucela-1",
                ["49°28'05.61''N, 17°02'23.09''E",
                 "49°27'43.146''N, 17°0'52.154''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/292-mala-becva-1",
                ["49°19'03.74''N, 17°23'07.82''E",
                 "49°22'35.28''N, 17°20'07.50''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/293-mala-becva-1a",
                ["49°22'44.24''N, 17°21'22.87''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/294-markovka-1",
                ["49°11'37.46''N, 15°54'45.06''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/295-mocla-1",
                ["49°04'43.31''N, 16°04'31.15''E",
                 "49°08'01.11''N, 16°02'20.45''E",
                 "49°07'15.84''N, 16°04'13.49''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/296-mocla-1m",
                ["49°05'11.68''N, 16°00'37.42''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/297-mocla-2",
                ["49°07'19.95''N, 16°04'01.16''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/298-morava-2",
                ["48°41'34.94''N, 16°59'46.59''E",
                 "48°44'06.77''N, 17°01'16.28''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/299-morava-3",
                ["48°44'06.77''N, 17°01'16.28''E",
                 "48°47'08.72''N, 17°05'17.78''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/300-morava-4",
                ["48°47'08.72''N, 17°05'17.78''E",
                 "48°50'33.98''N, 17°08'33.11''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/301-morava-4a",
                ["48°48'32.33''N, 17°06'17.39''E",
                 "48°50'51.61''N, 17°09'05.18''E",
                 "48°50'38.82''N, 17°09'00.11''E",
                 "48°51'43.00''N, 17°10'33.78''E",
                 "48°50'25.60''N, 17°05'16.34''E",
                 "48°50'42.63''N, 17°08'07.72''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/302-morava-4b",
                ["48°54'53.62''N, 17°06'11.05''E",
                 "48°54'53.62''N, 17°06'20.15''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/303-morava-4c",
                ["48°54'52.04''N, 17°10'00.02''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/304-morava-5",
                ["48°50'33.98''N, 17°08'33.11''E",
                 "48°53'17.27''N, 17°12'52.24''E",
                 "48°52'41.85''N, 17°12'7.66''E",
                 "48°52'34.63''N, 17°14'20.51''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/305-morava-6",
                ["48°53'17.27''N, 17°12'52.24''E",
                 "48°55'53.05''N, 17°19'20.84''E",
                 "48°52'34.63''N, 17°14'20.51''E",
                 "48°55'44.98''N, 17°19'17.91''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/306-morava-6a",
                ["48°53'25.31''N, 17°13'48.69''E",
                 "48°53'30.41''N, 17°16'30.32''E",
                 "48°55'43.16''N, 17°17'57.56''E",
                 "48°53'13.58''N, 17°28'01.17''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/307-morava-6m",
                ["48°52'03.61''N, 17°24'28.59''E",
                 "48°58'31.03''N, 17°15'34.99''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/308-morava-7",
                ["48°55'53.05''N, 17°19'20.84''E",
                 "48°58'08.89''N, 17°22'45.79''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/309-morava-7a",
                ["48°58'20.10''N, 17°22'39.05''E",
                 "48°58'18.81''N, 17°22'29.73''E",
                 "48°57'51.93''N, 17°22'54.33''E",
                 "48°58'03.90''N, 17°22'53.62''E",
                 "48°57'45.64''N, 17°22'59.54''E",
                 "48°58'11.54''N, 17°21'57.12''E",
                 "48°56'51.02''N, 17°21'56.41''E",
                 "48°58'40.44''N, 17°19'02.14''E",
                 "48°55'56.22''N, 17°19'24.52''E",
                 "48°56'24.41''N, 17°20'53.01''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/310-morava-8",
                ["48°58'08.89''N, 17°22'45.79''E",
                 "49°01'04.86''N, 17°23'21.61''E",
                 "48°58'54.54''N, 17°23'25.61''E",
                 "48°58'20.85''N, 17°26'49.65''E",
                 "48°59'37.47''N, 17°23'23.33''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/311-morava-8a",
                ["48°58'53.281\"N, 17°22'58.616\"E",
                 "48°58'40.87''N, 17°23'27.57''E",
                 "49°00'23.60''N, 17°23'50.28''E",
                 "48°58'45.95''N, 17°23'26.03''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/312-morava-9",
                ["49°01'04.86''N, 17°23'21.61''E",
                 "49°4'23.39''N, 17°27'30.44''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/313-morava-9a",
                ["49°03'55.72''N, 17°24'52.36''E",
                 "49°03'54.39''N, 17°25'09.50''E",
                 "49°4'13.11''N, 17°25'52.26''E",
                 "49°4'15.54''N, 17°25'40.75''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/314-morava-9b",
                ["49°03'12.05''N, 17°24'36.11''E",
                 "49°02'58.87''N, 17°24'34.29''E",
                 "49°02'33.64''N, 17°24'51.20''E",
                 "49°2'12.43''N, 17°23'47.19''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/315-morava-9c",
                ["49°04'56.62''N, 17°27'22.20''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/316-morava-10",
                ["49°04'23.39''N, 17°27'30.44''E",
                 "49°08'07.13''N, 17°30'08.09''E",
                 "49°04'24.63''N, 17°27'14.22''E",
                 "49°08'07.05''N, 17°30'04.13''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/317-morava-10a",
                ["49°06'17.66''N, 17°29'36.53''E",
                 "49°04'40.14''N, 17°28'29.67''E",
                 "49°05'30.01''N, 17°29'32.47''E",
                 "49°05'42.92''N, 17°29'04.21''E",
                 "49°06'02.55''N, 17°28'58.74''E",
                 "49°06'13.44''N, 17°29'05.59''E",
                 "49°06'39.27''N, 17°29'07.82''E",
                 "49°07'01.73''N, 17°29'09.78''E",
                 "49°07'17.49''N, 17°29'25.62''E",
                 "49°04'26.59''N, 17°28'35.36''E",
                 "49°07'54.15''N, 17°35'26.22''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/318-morava-11",
                ["49°08'07.13''N, 17°30'08.09''E",
                 "49°11'20.57''N, 17°30'47.39''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/319-morava-12",
                ["49°11'20.57''N, 17°30'47.39''E",
                 "49°13'05.01''N, 17°30'07.60''E",
                 "49°13'01.51''N, 17°30'10.69''E",
                 "49°16'27.66''N, 17°28'32.62''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/320-morava-12a",
                ["49°11'33.10''N, 17°30'59.15''E",
                 "49°15'42.72''N, 17°29'50.14''E",
                 "49°11'35.19''N, 17°30'33.11''E",
                 "49°13'21.26''N, 17°29'57.34''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/324-morava-12m",
                ["49°13'03.59\"N, 17°30'16.03\"E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/321-morava-13",
                ["49°13'05.01''N, 17°30'07.6''E",
                 "49°20'17.36''N, 17°20'49.14''E",
                 "49°16'09.68''N, 17°27'49.15''E",
                 "49°19'21.30\"N, 17°29'57.30\"E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/322-morava-13a",
                ["49°18'35.29''N, 17°23'17.84''E",
                 "49°17'14.19''N, 17°24'32.84''E",
                 "49°16'18.3\"N, 17°28'45\"E",
                 "49°17'55.72''N, 17°26'26.49''E",
                 "49°12'43.68''N, 17°24'08.66''E",
                 "49°18'18.76''N, 17°24'41.04''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/325-morava-13b",
                ["49°18'39.04\"N, 17°23'06.20\"E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/323-morava-13c",
                ["49°15'17.04''N, 17°28'48.78''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/326-mysluvka-1",
                ["49°7'50.34''N, 15°27'12.50''E",
                 "49°13'07.59''N, 15°21'39.45''E",
                 "49°11'26.440''N, 15°21'23.074''E",
                 "49°10'17.96\" N, 15°19'27.16\" E",
                 "49°11'35.982\"N 15°21'9.663\"E",
                 "49°11'27.299\"N 15°19'3.556\"E",
                 "49°11'15.460\"N 15°21'39.674\"E",
                 "49°12'27.997''N, 15°20'8.39''E",
                 "49°11'18.185''N, 15°23'3.259''E",
                 "49°12'12.222''N, 15°23'25.67''E",
                 "49°10'45.30''N, 15°24'12.32''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/327-mysluvka-1m",
                ["49°10'47.86''N, 15°24'24.38''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/328-navesni-rybnik",
                ["49°22'43.986\"N, 16°45'58.077\"E"]
            ],

            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/329-okluka-1",
                ["48°59'01.82''N, 17°25'06.94''E",
                 "48°54'03.86''N, 17°38'05.67''E",
                 "48°58'48.96''N, 17°30'50.95''E",
                 "48°55'39.74''N, 17°34'42.69''E",
                 "48°58'16.50''N, 17°31'59.18''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/330-olesnicky-potok-1a",
                ["49°33'50.98''N, 16°26'04.10''E",
                 "49°31'10.00''N, 16°26'50.37''E",
                 "49°32'39.77''N, 16°26'14.65''E",
                 "49°34'17.89''N, 16°26'03.39''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/331-olsava-1",
                ["49°02'51.16''N, 17°24'59.44''E",
                 "49°02'30.96''N, 17°33'25.76''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/332-olsava-1a",
                ["49°01'05.29''N, 17°25'34.39''E",
                 "49°00'42.36''N, 17°24'38.82''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/333-olsava-1b",
                ["49°01'17.70''N, 17°24'54.17''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/334-olsava-2",
                ["49°02'30.96''N, 17°33'25.76''E",
                 "49°1'13.85''N, 17°44'55.35''E",
                 "49°02'02.51''N, 17°41'22.36''E",
                 "49°4'29.65''N, 17°42'48.47''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/335-olsava-2a",
                ["48°58'01.84''N, 17°43'57.55''E",
                 "48°56'45.03''N, 17°40'51.72''E",
                 "48°54'31.77''N, 17°44'19.20''E",
                 "48°54'26.22''N, 17°40'32.04''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/336-olsava-3a",
                ["49°01'29.88''N, 17°49'18.20''E",
                 "49°1'40.32''N, 17°48'15.97''E",
                 "49°01'27.86''N, 17°45'45.93''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/337-oslava-1",
                ["49°05'51.19''N, 16°21'51.21''E",
                 "49°07'48.55''N, 16°16'56.46''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/338-oslava-1m",
                ["49°06'13.27''N, 16°21'44.40''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/339-oslava-2",
                ["49°07'48.85''N, 16°16'56.46''E",
                 "49°08'41.74''N, 16°11'47.01''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/340-oslava-3",
                ["49°08'41.74''N, 16°11'47.01''E",
                 "49°16'11.35''N, 16°05'01.58''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/341-oslava-4",
                ["49°13'03.70''N, 16°10'26.64''E",
                 "49°12'13.05''N, 16°08'31.95''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/342-oslava-4m",
                ["49°12'21.72''N, 16°06'13.16''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/343-oslava-5",
                ["49°16'11.35''N, 16°05'01.58''E",
                 "49°18'43.19''N, 16°1'46.15''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/344-oslava-6a",
                ["49°19'48.18''N, 15°58'36.79''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/345-oslava-7",
                ["49°23'42.255''N, 16°00'49.913''E",
                 "49°27'53.177''N, 15°58'23.727''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/346-oslava-7a",
                ["49°25'58.740\"N, 16°2'19.691\"E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/347-oslava-8",
                ["49°27'53.177''N, 15°58'23.727''E",
                 "49°30'27.47''N, 15°58'59.27''E",
                 "49°29'14.28''N, 15°59'16.47''E",
                 "49°29'40.38''N, 15°55'34.13''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/348-pavov-1",
                ["49°26'28.79''N, 15°35'46.18''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/349-podomsky-potok-1",
                ["49°20'19.63''N, 16°49'40.11''E",
                 "49°20'19.45''N, 16°43'8.80''E",
                 "49°20'08.61''N, 16°43'21.26''E",
                 "49°20'55.07''N, 16°39'02.25''E",
                 "49°22'20.61''N, 16°40'25.26''E",
                 "49°25'51.51''N, 16°35'03.36''E",
                 "49°23'25.10''N, 16°37'15.78''E",
                 "49°23'59.59''N, 16°43'16.79''E",
                 "49°26'22.25''N, 16°40'0.78''E",
                 "49°24'12.11''N, 16°42'12.64''E",
                 "49°25'55.33''N, 16°48'09.40''E",
                 "49°22'01.02''N, 16°39'33.44''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/350-podomsky-potok-1a",
                ["49°22'41.39''N, 16°40'39.03''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/351-podomsky-potok-1b",
                ["49°25'43.98''N, 16°45'24.90''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/352-prusanecky-potok-1",
                ["48°50'20.68''N, 16°55'45.76''E",
                 "48°55'27.29''N, 16°55'33.31''E",
                 "48°51'45.66''N, 16°54'55.52''E",
                 "48°51'55.29''N, 16°52'58.85''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/237-chlumsky-potok-1a",
                [
                     "49°13´31\"N, 17°36´48\"E",
                     "49°13´36\"N, 17°36´48\"E"
                ]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/238-ivanovicky-potok-1",
                ["49°05'35.73''N, 16°37'12.53''E",
                 "49°09'32.93''N, 16°39'30.92''E",
                 "49°09'18.57\"N, 16°38'35.03\"E",
                 "49°09'13.54\"N, 16°38'39.89\"E",
                 "49°09'10.69\"N, 16°38'41.75\"E",
                 "49°09'03.79\"N, 16°38'40.24\"E",
                 "49°08'57.57\"N, 16°38'36.84\"E",
                 "49°08'52.02\"N, 16°38'33.94\"E",
                 "49°08'48.20\"N, 16°38'33.29\"E",
                 "49°08'48.10\"N, 16°38'38.89\"E",
                 "49°08'44.99\"N, 16°38'41.78\"E",
                 "49°08'44.84\"N, 16°38'37.46\"E",
                 "49°08'02.80''N, 16°38'34.22''E",
                 "49°08'00.70''N, 16°38'34.25''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/239-janustice-1a",
                ["49°17'36.99''N, 17°43'34.85''E",
                 "49°17'28.46''N, 17°43'31.11''E",
                 "49°17'45.39''N, 17°42'04.59''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/240-jaromerice-1",
                ["49°05'21.57''N, 15°52'56.49''E",
                 "49°05'33.87''N, 15°39'41.12''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/241-jaromerice-1a",
                ["48°58'24.33''N, 15°54'54.12''E",
                 "49°00'51.13''N, 15°49'04.54''E",
                 "49°03'16.00''N, 15°49'07.95''E",
                 "48°58'34.70\"N, 15°54'20.36\"E",
                 "49°0'37.60''N,  15°46'22.02''E"
                 ]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/783-jaromerice-1b",
                ["48°58'14.779\"N, 15°51'14.756\"E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/242-jaromerice-1m",
                ["49°02'10.13''N, 15°50'09.15''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/243-jevisovka-1",
                ["48°49'40.42''N, 16°28'20.05''E",
                 "48°54'24.56''N, 16°11'41.61''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/244-jevisovka-1a",
                ["48°48'56.76''N, 16°23'33.09''E",
                 "48°49'37.09''N, 16°24'1.94''E",
                 "48°49'05.57''N, 16°17'23.43''E",
                 "48°45'53.85''N, 16°21'15.97''E",
                 "48°45'54.69''N, 16°23'11.11''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/245-jevisovka-2",
                ["48°54'24.56''N, 16°11'41.61''E",
                 "48°59'31.31''N, 15°58'48.29''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/246-jevisovka-2a",
                ["48°55'44.74''N, 16°06'24.47''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/247-jevisovka-3",
                ["48°59'29.99''N, 15°58'48.36''E",
                 "48°58'56.59''N, 15°55'29.32''E",
                 "48°59'28.88''N, 15°58'38.65''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/248-jihlava-1",
                ["48°55'03.23''N, 16°35'56.32''E",
                 "48°59'35.68''N, 16°31'05.02''E",
                 "48°57'45.59''N, 16°34'02.38''E"]
            ],
            [

                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/249-jihlava-1m",
                ["48°58'53.53''N, 16°31'17.62''E",
                 "48°58'18.15''N, 16°20'18.67''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/250-jihlava-2",
                ["48°59'35.68''N, 16°31'05.02''E",
                 "49°02'17.27\"N, 16°30'33.51\"E",
                 "49°01'59.21''N, 16°31'04.90''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/251-jihlava-3",
                ["49°02'17.27\"N, 16°30'33.51\"E",
                 "49°04'55.64''N, 16°24'37.78''E",
                 "49°04'31.58''N, 16°26'40.72''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/252-jihlava-4",
                ["49°04'55.64''N, 16°24'37.78''E",
                 "49°05'50.91''N, 16°21'51.47''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/785-jihlava-4a",
                [
                    "49'05'29.30”N, 16‘20'42.60”E"
                ]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/253-jihlava-5m",
                ["49°05'39.14''N, 16°16'50.68''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/254-jihlava-6",
                ["49°06'08.89''N, 16°10'50.16''E",
                 "49°07'30.48''N, 16°07'20.56''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/267-jihlava-6a",
                ["49°06'22.16''N, 16°09'27.96''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/255-jihlava-7-8",
                ["49°07'30.48''N, 16°07'20.56''E",
                 "49°12'24.55''N, 15°59'52.06''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/256-jihlava-9",
                ["49°12'24.55''N, 15°59'52.06''E",
                 "49°12'56.64''N, 15°51'13.94''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/257-jihlava-10",
                ["49°12'56.64''N, 15°51'13.94''E",
                 "49°15'20.11\"N, 15°46'53.25\"E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/258-jihlava-11",
                ["49°15'20.11\"N, 15°46'53.25\"E",
                 "49°18'27.32''N, 15°44'52.07''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/259-jihlava-12",
                ["49°18'27.32''N, 15°44'52.07''E",
                 "49°22'41.745''N, 15°39'44.504''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/260-jihlava-13",
                ["49°22'41.475''N, 15°39'44.504''E",
                 "49°24'22.26''N, 15°34'51.47''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/261-jihlava-13a",
                ["49°23'20.81''N, 15°36'10.19''E",
                 "49°23'38.52''N, 15°31'32.53''E",
                 "49°20'27.52''N, 15°33'48.63''E",
                 "49°26'51.98''N, 15°33'01.47''E",
                 "49°26'43.90''N, 15°32'45.29''E",
                 "49°25'08.88''N, 15°34'19.98''E",
                 "49°23'32.47''N, 15°33'23.45''E",
                 "49°27'21.71''N, 15°37'15.94''E",
                 "49°20'34.72''N, 15°34'0.83''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/266-jihlava-13b",
                ["49°25'39.56''N, 15°35'52.83''E",
                 "49°23'24.050\"N, 15°33'5.667\"E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/262-jihlava-13c",
                ["49°23'15.49''N, 15°33'11.70''E",
                 "49°22'58.57''N, 15°33'00.97''E",
                 "49°23'25.18''N, 15°32'56.86''E",
                 "49°22'41.17''N, 15°33'02.63''E",
                 "49°22'33.51''N, 15°33'08.10''E",
                 "49°22'26.74''N, 15°32'54.19''E",
                 "49°23'07.83''N, 15°32'27.81''E",
                 "49°23'09.78''N, 15°32'05.21''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/263-jihlava-14",
                ["49°24'22.26''N, 15°34'51.47''E",
                 "49°21'30.506''N, 15°29'10.224''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/264-jihlava-15",
                ["49°21'30.506''N, 15°29'10.224''E",
                 "49°15'44.09''N, 15°16'45.94''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/265-jihlava-15a",
                ["49°18'43.09''N, 15°22'44.82''E",
                 "49°19'01.03''N, 15°19'32.77''E",
                 "49°19'19.17''N, 15°18'46.22''E",
                 "49°21'00.16''N, 15°26'25.91''E",
                 "49°18'47.93''N, 15°19'51.43''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/268-klimsak-1",
                ["49°24'24.90''N, 16°39'53.33''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/269-klimsak-1m",
                ["49°24'31.25''N, 16°38'09.27''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/270-kockuv-rybnik-1",
                ["49°30'49.50''N, 16°36'04.93''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/271-kovalovicky-potok-1",
                ["49°12'30.06''N, 16°48'39.87''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/272-kretinka-1",
                ["49°33'13.58''N, 16°33'23.72''E",
                 "49°33'57.95''N, 16°30'23.40''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/273-krovacka-1",
                ["49°08'28.90\"N, 17°00'26.70\"E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/274-kyjovka-2",
                ["48°42'15.35''N, 16°57'08.28''E",
                 "48°43'53.67''N, 16°58'44.18''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/275-kyjovka-2-1",
                ["48°43'53.67''N, 16°58'44.18''E",
                 "48°45'25.19''N, 16°59'56.01''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/276-kyjovka-2-2",
                ["48°45'25.19''N, 16°59'56.01''E",
                 "48°47'42.92''N, 17°02'11.59''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/277-kyjovka-2a",
                ["48°44'19.13''N, 16°55'40.23''E",
                 "48°43'11.12''N, 16°56'57.07''E",
                 "48°42'57.49''N, 16°56'34.03''E",
                 "48°43'01.39''N, 16°56'29.19''E",
                 "48°43'42.51''N, 16°59'03.76''E",
                 "48°43'34.27''N, 16°58'49.53''E",
                 "48°42'50.75''N, 16°57'52.23''E",
                 "48°42'31.95''N, 16°57'56.58''E",
                 "48°42'19.16''N, 16°57'32.01''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/278-kyjovka-2b",
                ["48°47'42.92''N, 17°02'11.59''E",
                 "48°50'47.87''N, 17°05'19.08''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/279-kyjovka-2c",
                ["48°44'55.14''N, 16°56'11.87''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/280-kyjovka-2c-1",
                ["48°43'55.96''N, 16°55'19.86''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/281-kyjovka-2d",
                ["48°44'10.67''N, 17°00'58.86''E",
                 "48°44'30.08''N, 17°01'29.51''E",
                 "48°44'46.07''N, 17°01'39.11''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/282-kyjovka-2e",
                ["48°47'00.62''N, 17°04'54.94''E",
                 "48°46'07.14''N, 17°02'51.13''E",
                 "48°46'12.72''N, 17°03'09.94''E",
                 "48°46'23.30''N, 17°03'25.82''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/283-kyjovka-3",
                ["48°55'58.39''N, 17°03'57.26''E",
                 "49°06'40.96''N, 17°08'31.67''E",
                 "48°59'29.15''N, 17°01'54.05''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/284-kyjovka-3a",
                ["49°00'58.31''N, 17°10'56.54''E",
                 "49°01'29.65''N, 17°12'12.27''E",
                 "49°02'01.15''N, 17°13'27.30''E",
                 "48°58'08.34''N, 17°04'59.74''E",
                 "48°59'27.53''N, 17°06'15.09''E",
                 "48°59'32.41''N, 17°06'16.38''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/285-kyjovka-3b",
                ["49°04'19.13''N, 17°03'13.43''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/286-kyjovka-3c",
                ["49°02'22.06''N, 17°11'02.90''E",
                 "49°03'00.19''N, 17°11'02.96''E",
                 "48°57'23''N, 17°08'14''E"
                 ]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/287-kyjovka-4a",
                ["49°03'36.60''N, 17°14'21.93''E",
                 "49°04'14.93''N, 17°13'24.16''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/288-lisenska-ricka-1",
                ["49°04'17.91''N, 16°41'33.91''E",
                 "49°13'15.55''N, 16°42'50.60''E",
                 "49°13'0.22''N, 16°43'8.57''E",
                 "49°12'43.93''N, 16°42'41.37''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/289-loucka-1a",
                ["49°21'31.43''N, 16°20'35.44''E",
                 "49°22'15.18''N, 16°20'17.44''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/290-loucka-4a",
                ["49°34'47.70''N, 16°03'49.08''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/291-lubi-1",
                []
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/354-rakovec-1",
                ["49°07'37.55''N, 16°50'23.13''E",
                 "49°11'12.67''N, 16°51'10.11''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/355-rakovec-2",
                ["49°11'12.67''N, 16°51'10.11''E",
                 "49°16'12.19''N, 16°54'10.34''E",
                 "49°15'47.98''N, 16°55'39.91''E",
                 "49°19'23.80''N, 16°50'56.47''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/356-roketnice-1",
                ["49°09'08.20''N, 16°44'15.52''E",
                 "49°13'58.66''N, 16°47'33.88''E",
                 "49°09'21.83''N, 16°44'42.31''E",
                 "49°05'02.35''N, 16°43'49.11''E",
                 "49°09'34.070''N, 16°45'1.805''E",
                 "49°09'58.476''N, 16°45'19.655''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/357-rokytna-1",
                ["49°05'48.57''N, 16°23'00.48''E",
                 "49°01'42.89''N, 16°18'28.36''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/358-rokytna-1m",
                ["48°59'53.21''N, 16°11'32.88''E",
                 "49°03'31.46''N, 16°15'26.97''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/359-rokytna-2",
                ["49°01'42.59''N, 16°18'28.36''E",
                 "49°01'40.51''N, 16°13'11.01''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/360-rokytna-3",
                ["49°01'40.51''N, 16°13'11.01''E",
                 "49°02'17.67''N, 16°06'04.09''E",
                 "49°02'47.24''N, 16°08'43.90''E",
                 "49°4'43.42''N, 16°4'30.83''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/361-rokytna-3a",
                ["49°01'32.40''N, 16°08'14.45''E",
                 "49°03'54.59''N, 16°8'57.67''E",
                 "49°01'50.77''N, 16°06'26.42''E",
                 "49°00'01.26''N, 16°08'54.02''E",
                 "49°04'35.93''N, 16°07'23.78''E",
                 "48°57'56.85''N, 16°07'31.13''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/362-rokytna-4",
                ["49°02'17.67''N, 16°06'04.09''E",
                 "49°07'04.27''N, 15°49'56.33''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/363-rokytna-5",
                ["49°07'33.07''N, 15°53'21.47''E",
                 "49°05'43.70''N, 15°54'59.60''E",
                 "49°06'06.47''N, 15°53'23.74''E",
                 "49°06'15.06''N, 15°55'42.62''E",
                 "49°02'21.94''N, 15°59'06.02''E",
                 "49°07'00.64''N, 15°55'13.77''E",
                 "49°03'14.38''N, 16°02'33.22''E",
                 "49°06'09.36''N, 15°56'30.23''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/365-rokytna-5m",
                ["49°05'19.87''N, 15°54'27.97''E",
                 "49°05'30.39''N, 15°53'03.03''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/364-rokytna-6",
                ["49°07'04.27''N, 15°49'53.33''E",
                 "49°11'51.23''N, 15°44'32.51''E",
                 "49°09'59.01''N, 15°45'28.68''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/769-rokytna-6a",
                ["49°09'24.17''N, 15°55'01.79''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/366-romze-3a",
                ["49°38'38.91''N, 16°53'35.90''E",
                 "49°33'00.67''N, 16°57'00.15''E",
                 "49°35'37''N, 16°56'07''E",
                 "49°35'43.7''N, 16°53'34.66''E",
                 "49°36'24.13''N, 16°53'25.57''E",
                 "49°35'59.67''N, 16°49'08.60''E",
                 "49°36'3.11''N, 16°55'39.72''E",
                 "49°34'03.60''N, 17°00'20.45''E",
                 "49°38'28.24''N, 16°50'44.22''E",
                 "49°35'4.33''N, 16°48'11.45''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/367-romze-3c",
                ["49°34'29.36''N, 16°48'54.71''E",
                 "49°34'34.63''N, 16°49'12.48''E",
                 "49°34'36.83''N, 16°49'15.41''E",
                 "49°35'12.29''N, 16°49'5.29''E",
                 "49°35'32.47''N, 16°48'54.63''E",
                 "49°32'49.6\"N, 16°49'58.2\"E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/368-romze-3d",
                ["49°36'53.47\"N, 16°50'17.67\"E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/369-rostenicky-potok-1",
                ["49°16'34.71''N, 17°00'16.05''E",
                 "49°11'53.70''N, 17°2'40.26''E",
                 "49°15'52.2\"N, 16°59'30.99\"E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/370-rusava-2",
                ["49°20'16.9\"N, 17°35'04.19\"E",
                 "49°20'18.36\"N, 17°35'08.59\"E",
                 "49°20'20.42\"N, 17°35'16.32\"E",
                 "49°20'50.94''N, 17°36'12.30''E",
                 "49°20'07.48''N, 17°43'20.24''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/371-rusava-2a",
                ["49°24'13.48''N, 17°36'28.35''E",
                 "49°24'50.03''N, 17°37'54.57''E",
                 "49°25'11.14''N, 17°41'07.18''E",
                 "49°24'04.24''N, 17°40'38.17''E",
                 "49°24'50.62''N, 17°39'10.85''E",
                 "49°25'23.34''N, 17°45'06.37''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/372-rusava-2b",
                ["49°20'04.03''N, 17°35'06.22''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/373-sazava-17",
                ["49°33'53.96''N, 15°53'57.31''E",
                 "49°34'46.05''N, 15°55'56.28''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/374-sazava-18",
                ["49°34'48.62''N, 15°55'58.73''E",
                 "49°35'02.90''N, 15°55'58.13''E",
                 "49°34'52.01''N, 15°56'8.87''E",
                 "49°34'53.12''N, 15°56'02.20''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/376-sazava-19",
                ["49°35'17.89''N, 15°55'46.89''E",
                 "49°36'31.28''N, 15°54'59.92''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/377-starecsky-potok-1",
                ["49°12'58.87''N, 15°52'36.74''E",
                 "49°14'57.09''N, 15°42'50.47''E",
                 "49°10'33.19''N, 15°54'02.16''E",
                 "49°14'26.57''N, 15°46'04.18''E",
                 "49°11'41.65''N, 15°45'02.93''E",
                 "49°12'51.79''N, 15°39'07.14''E",
                 "49°14'24.28''N, 15°45'47.82''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/378-starecsky-potok-1a",
                ["49°17'50.22''N, 15°52'53.59''E",
                 "49°17'36.69''N, 15°54'45.00''E",
                 "49°16'30.91''N, 16°0'41.48''E",
                 "49°16'31.31''N, 16°0'36.92''E",
                 "49°16'31.77''N, 16°00'30.58''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/379-starecsky-potok-1b",
                ["49°16'56.32''N, 16°01'18.13''E",
                 "49°16'51.63''N, 16°01'21.50''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/380-svitava-1",
                ["49°08'30.91''N, 16°37'41.74''E",
                 "49°15'06.62''N, 16°40'13.91''E",
                 "49°14'2.574''N, 16°40'12.166''E",
                 "49°15'6.525''N, 16°40'13.953''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/382-svitava-3a",
                ["49°22'13.49\"N, 16°39'00.834\"E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/381-svitava-5a",
                ["49°33'10.38''N, 16°35'7.35''E",
                 "49°36'42.44''N, 16°34'46.99''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/383-svratka-1",
                ["48°55'10.53''N, 16°36'20.92''E",
                 "48°58'09.87''N, 16°39'08.20''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/384-svratka-1a",
                ["48°58'21.64''N, 16°36'32.52''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/385-svratka-1m",
                ["48°57'49.07''N, 16°38'23.49''E",
                 "48°57'44.18''N, 16°37'48.91''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/386-svratka-2",
                ["48°58'09.87''N, 16°39'08.20''E",
                 "49°02'26.09''N, 16°36'55.55''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/395-svratka-2b",
                ["49°04'22.95''N, 16°32'56.45''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/387-svratka-3",
                ["49°02'26.09''N, 16°36'55.55''E",
                 "49°11'56.79''N, 16°34'0.03''E",
                 "49°05'52.00''N, 16°36'55.72''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/388-svratka-4",
                ["49°11'56.79''N, 16°34'0.03''E",
                 "49°13'56.56''N, 16°31'08.26''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/389-svratka-5",
                ["49°13'56.56''N, 16°31'08.26''E",
                 "49°16'37.69''N, 16°27'05.53''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/390-svratka-6",
                ["49°16'37.69''N, 16°27'05.53''E",
                 "49°19'26.93''N, 16°25'35.92''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/391-svratka-7-8a",
                ["49°21'15.94''N, 16°23'55.61''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/392-svratka-11m",
                ["49°33'09.87''N, 16°19'55.76''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/393-svratka-14a",
                ["49°41'7.74''N, 16°3'38.45''E",
                 "49°43'35.72''N, 16°02'29.55''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/394-svratka-14m",
                ["49°41'58.51''N, 15°58'25.29''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/396-scavnice-2a",
                ["49°09'52.32''N, 17°51'37.40''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/397-svabovsky-potok-1",
                ["49°19'01.39''N, 15°21'02.23''E",
                 "49°15'50.18''N, 15°20'2.853''E",
                 "49°18'21.01''N, 15°21'55.23''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/398-trkmanka-1",
                ["48°48'51.01''N, 16°50'00.26''E",
                 "48°50'58.92''N, 16°49'53.94''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/399-trkmanka-2",
                ["48°50'58.92''N, 16°49'53.94''E",
                 "49°05'09.09''N, 17°00'28.39''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/400-trestsky-potok-1",
                ["49°20'38.03''N, 15°29'26.39''E",
                 "49°14'09.57''N, 15°20'18.25''E",
                 "49°16'43.67''N, 15°26'13.77''E",
                 "49°16'15.54''N, 15°28'07.59''E",
                 "49°17'57.26''N, 15°29'53.78''E",
                 "49°18'26.98''N, 15°29'35.93''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/401-valcha-1",
                ["49°16'50.97''N, 15°28'21.64''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/402-valcha-2",
                ["49°16'45.76''N, 15°27'55.85''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/403-valova-2",
                ["49°26'25.56''N, 17°11'20.27''E",
                 "49°30'48.68''N, 17°02'18.63''E",
                 "49°29'51.61''N, 17°03'46.56''E",
                 "49°29'45.15''N, 17°05'21.20''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/779-vapovka-2",
                ["49°06'58.45''N, 15°31'43.95''E",
                 "49°10'46.35''N, 15°35'12.05''E",
                 "49°11'24.57''N, 15°33'07.96''E",
                 "49°11'25.03''N, 15°33'07.96''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/404-velicka-1",
                ["48°54'30.66''N, 17°16'11.93''E",
                 "48°54'40.55''N, 17°29'54.89''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/405-velicka-1m",
                ["48°54'13.42''N, 17°26'57.99''E",
                 "48°54'19.84''N, 17°26'07.06''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/406-velicka-2",
                ["48°54'40.55''N, 17°29'54.89''E",
                 "48°51'57.29''N, 17°31'53.83''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/416-vicemilice-1",
                ["49°08'12.70\"N, 17°01'23.50\"E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/407-vlara-1",
                ["49°01'53.30''N, 18°03'06.63''E",
                 "49°06'00.29''N, 17°55'58.33''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/408-vlara-1a",
                ["49°05'21.35''N, 17°57'51.55''E",
                 "49°05'32.35''N, 17°52'45.81''E",
                 "49°05'45.81''N, 17°52'53.00''E",
                 "49°08'16.58''N, 18°01'13.72''E",
                 "49°07'35.34''N, 18°04'20.36''E",
                 "49°09'49.77''N, 18°02'28.61''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/409-vracov-1",
                ["48°58'37.08''N, 17°12'14.25''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/410-zdarna-1",
                ["49°24'23.96''N, 16°44'17.36''E",
                 "49°30'21.04''N, 16°47'23.27''E",
                 "49°30'56.60''N, 16°47'19.19''E",
                 "49°34'26.65''N, 16°44'11.71''E",
                 "49°30'23.38''N, 16°31'15.98''E",
                 "49°30'25.39''N, 16°30'00.06''E",
                 "49°29'10.08''N, 16°45'40.66''E",
                 "49°34'55.691\"N, 16°43'1.264\"E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/411-zeletavka-1",
                ["48°57'41.93''N, 15°41'03.82''E",
                 "48°57'47.53''N, 15°35'19.31''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/412-zeletavka-1a",
                ["48°58'16.18''N, 15°37'24.33''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/413-zeletavka-2",
                ["48°57'47.53\"N, 15°35'19.31\"E",
                 "49°10'17.34''N, 15°39'32.64''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/414-zeletavka-2a",
                ["49°04'53.05''N, 15°35'06.67''E",
                 "49°04'42.46''N, 15°32'00.20''E",
                 "49°00'51.50''N, 15°34'48.08''E",
                 "49°00'53.76''N, 15°34'38.95''E",
                 "49°02'40.77''N, 15°33'54.81''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/415-zeletavka-2b",
                ["49°08'53.56''N, 15°40'23.27''E",
                 "49°08'04.95''N, 15°39'38.83''E"]
            ],
            [
                "http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/778-zeletavka-2c",
                ["49°1'54.80''N, 15°33'59.90''E"]
            ]
        ]
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
