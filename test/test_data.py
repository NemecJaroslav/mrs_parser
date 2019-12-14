def zip_lists(list_1, list_2):
    result = []
    for item_1, item_2 in zip(list_1, list_2):
        result.append([item_1, item_2])
    return result


def get_expected_locations():
    locations_short = [
        # B
        "176-bacicky-potok",
        "177-balas-1a",
        "178-balinka-1",
        "179-balinka-1a",
        "180-balinka-1b",
        "181-bily-potok-2a",
        "182-blata-3",
        "183-bobrava-1",
        "184-bobrava-2",
        "185-bobrava-2a",
        "186-brodecky-potok-1",
        "187-brtnice-1",
        "188-brtnice-1a",
        "189-buchlovicky-potok-1",
        "190-buchlovicky-potok-1m",
        "191-bystrice-pernstejnska-2",
        "777-bykovka-1a",
        # C
        "192-cezava-1",
        "193-cezava-1a",
        "194-cezava-2",
        "195-cezava-2a",
        "196-cezava-3a",
        "197-cikhajsky-potok-1",
        # D
        "198-drevnice-1",
        "199-drevnice-1a",
        "200-dyje-2",
        "201-dyje-3",
        "202-dyje-3a",
        "203-dyje-4",
        "204-dyje-4a",
        "205-dyje-4b",
        "206-dyje-4c",
        "207-dyje-4c-1",
        "209-dyje-4d",
        "210-dyje-4e",
        "211-dyje-4g",
        "212-dyje-4m",
        "128-dyje-5",
        "213-dyje-5a",
        "130-dyje-7",
        "214-dyje-7a",
        "216-dyje-7b",
        "215-dyje-8",
        "217-dyje-9",
        "218-dyje-10",
        "219-dyje-11",
        "220-dyje-11a",
        "221-dyje-15",
        "222-dyje-19",
        "223-dyje-19a",
        "224-dyje-19b",
        "225-dyje-19c",
        # G
        "226-greslovomytsky-potok-1",
        # H
        "614-habrovansky-potok-1a",
        "227-hana-1",
        "228-hana-1a",
        "232-hana-1b",
        "229-hana-2",
        "230-hana-3",
        "231-hana-3m",
        "234-herdy",
        "233-hloucela-1",
        # M
        "292-mala-becva-1",
        "293-mala-becva-1a",
        "294-markovka-1",
        "295-mocla-1",
        "296-mocla-1m",
        "297-mocla-2",
        "298-morava-2",
        "299-morava-3",
        "300-morava-4",
        "301-morava-4a",
        "302-morava-4b",
        "303-morava-4c",
        "304-morava-5",
        "305-morava-6",
        "306-morava-6a",
        "307-morava-6m",
        "308-morava-7",
        "309-morava-7a",
        "310-morava-8",
        "311-morava-8a",
        "312-morava-9",
        "313-morava-9a",
        "314-morava-9b",
        "315-morava-9c",
        "316-morava-10",
        "317-morava-10a",
        "318-morava-11",
        "319-morava-12",
        "320-morava-12a",
        "324-morava-12m",
        "321-morava-13",
        "322-morava-13a",
        "325-morava-13b",
        "323-morava-13c",
        "326-mysluvka-1",
        "327-mysluvka-1m",
        # N
        "328-navesni-rybnik",
        # O
        "329-okluka-1",
        "330-olesnicky-potok-1a",
        "331-olsava-1",
        "332-olsava-1a",
        "333-olsava-1b",
        "334-olsava-2",
        "335-olsava-2a",
        "336-olsava-3a",
        "337-oslava-1",
        "338-oslava-1m",
        "339-oslava-2",
        "340-oslava-3",
        "341-oslava-4",
        "342-oslava-4m",
        "343-oslava-5",
        "344-oslava-6a",
        "345-oslava-7",
        "346-oslava-7a",
        "347-oslava-8",
        # P
        "348-pavov-1",
        "349-podomsky-potok-1",
        "350-podomsky-potok-1a",
        "351-podomsky-potok-1b",
        "352-prusanecky-potok-1",
        # CH
        "237-chlumsky-potok-1a",
        # I
        "238-ivanovicky-potok-1",
        # J
        "239-janustice-1a",
        "240-jaromerice-1",
        "241-jaromerice-1a",
        "783-jaromerice-1b",
        "242-jaromerice-1m",
        "243-jevisovka-1",
        "244-jevisovka-1a",
        "245-jevisovka-2",
        "246-jevisovka-2a",
        "247-jevisovka-3",
        "248-jihlava-1",
        "249-jihlava-1m",
        "250-jihlava-2",
        "251-jihlava-3",
        "252-jihlava-4",
        "785-jihlava-4a",
        "253-jihlava-5m",
        "254-jihlava-6",
        "267-jihlava-6a",
        "255-jihlava-7-8",
        "256-jihlava-9",
        "257-jihlava-10",
        "258-jihlava-11",
        "259-jihlava-12",
        "260-jihlava-13",
        "261-jihlava-13a",
        "266-jihlava-13b",
        "262-jihlava-13c",
        "263-jihlava-14",
        "264-jihlava-15",
        "265-jihlava-15a",
        # K
        "268-klimsak-1",
        "269-klimsak-1m",
        "270-kockuv-rybnik-1",
        "271-kovalovicky-potok-1",
        "272-kretinka-1",
        "273-krovacka-1",
        "274-kyjovka-2",
        "275-kyjovka-2-1",
        "276-kyjovka-2-2",
        "277-kyjovka-2a",
        "278-kyjovka-2b",
        "279-kyjovka-2c",
        "280-kyjovka-2c-1",
        "281-kyjovka-2d",
        "282-kyjovka-2e",
        "283-kyjovka-3",
        "284-kyjovka-3a",
        "285-kyjovka-3b",
        "286-kyjovka-3c",
        "287-kyjovka-4a",
        # L
        "288-lisenska-ricka-1",
        "289-loucka-1a",
        "290-loucka-4a",
        "291-lubi-1",
        # R
        "354-rakovec-1",
        "355-rakovec-2",
        "356-roketnice-1",
        "357-rokytna-1",
        "358-rokytna-1m",
        "359-rokytna-2",
        "360-rokytna-3",
        "361-rokytna-3a",
        "362-rokytna-4",
        "363-rokytna-5",
        "365-rokytna-5m",
        "364-rokytna-6",
        "769-rokytna-6a",
        "366-romze-3a",
        "367-romze-3c",
        "368-romze-3d",
        "369-rostenicky-potok-1",
        "370-rusava-2",
        "371-rusava-2a",
        "372-rusava-2b",
        # S
        "373-sazava-17",
        "374-sazava-18",
        "376-sazava-19",
        "377-starecsky-potok-1",
        "378-starecsky-potok-1a",
        "379-starecsky-potok-1b",
        "380-svitava-1",
        "382-svitava-3a",
        "381-svitava-5a",
        "383-svratka-1",
        "384-svratka-1a",
        "385-svratka-1m",
        "386-svratka-2",
        "395-svratka-2b",
        "387-svratka-3",
        "388-svratka-4",
        "389-svratka-5",
        "390-svratka-6",
        "391-svratka-7-8a",
        "392-svratka-11m",
        "393-svratka-14a",
        "394-svratka-14m",
        # S^
        "396-scavnice-2a",
        "397-svabovsky-potok-1",
        # T
        "398-trkmanka-1",
        "399-trkmanka-2",
        "400-trestsky-potok-1",
        # V
        "401-valcha-1",
        "402-valcha-2",
        "403-valova-2",
        "779-vapovka-2",
        "404-velicka-1",
        "405-velicka-1m",
        "406-velicka-2",
        "416-vicemilice-1",
        "407-vlara-1",
        "408-vlara-1a",
        "409-vracov-1",
        # Z
        "410-zdarna-1",
        "411-zeletavka-1",
        "412-zeletavka-1a",
        "413-zeletavka-2",
        "414-zeletavka-2a",
        "415-zeletavka-2b",
        "778-zeletavka-2c",
    ]
    return ["http://www.mrsbrno.cz/index.php/14-mimopstruhove-reviry/"
            + location_short for location_short in locations_short]


def get_expected_location_ids():
    identifiers = [
        "461 200",
        "461 209",
        "461 001",
        "461 180",
        "461 218",
        "461 188",
        "461 004",
        "461 005",
        "461 195",
        "461 162",
        "461 006",
        "461 007",
        "461 008",
        "461 009",
        "461 316",
        "461 010",
        "461 229",
        "461 011",
        "461 012",
        "461 013",
        "461 014",
        "461 015",
        "461 016",
        "461 017",
        "461 018",
        "461 019",
        "461 020",
        "461 021",
        "461 022",
        "461 023",
        "461 158",
        "461 159",
        "461 199",
        "461 176",
        "461 324",
        "461 326",
        "461 318",
        "461 024",
        "461 025",
        "461 026",
        "461 027",
        "461 184",
        "461 028",
        "461 029",
        "461 030",
        "461 031",
        "461 196",
        "461 032",
        "461 033",
        "461 034",
        "461 198",
        "461 219",
        "461 035",
        "461 221",
        "461 036",
        "461 165",
        "461 206",
        "461 037",
        "461 038",
        "461 309",
        "461 325",
        "461 039",
        "461 002",
        "461 003",
        "461 078",
        "461 079",
        "461 308",
        "461 322",
        "461 080",
        "461 081",
        "461 083",
        "461 084",
        "461 168",
        "461 177",
        "461 085",
        "461 086",
        "461 087",
        "461 302",
        "461 088",
        "461 089",
        "461 090",
        "461 091",
        "461 092",
        "461 093",
        "461 099",
        "461 210",
        "461 094",
        "461 095",
        "461 096",
        "461 098",
        "461 100",
        "461 327",
        "461 101",
        "461 102",
        "461 224",
        "461 103",
        "461 104",
        "461 317",
        "461 226",
        "461 105",
        "461 186",
        "461 106",
        "461 107",
        "461 108",
        "461 109",
        "461 110",
        "461 167",
        "461 111",
        "461 315",
        "461 169",
        "461 170",
        "461 112",
        "461 303",
        "461 161",
        "461 217",
        "461 113",
        "461 223",
        "461 114",
        "461 205",
        "461 115",
        "461 202",
        "461 212",
        "461 116",
        "461 323",
        "461 041",
        "461 042",
        "461 043",
        "461 044",
        "461 230",
        "461 320",
        "461 045",
        "461 046",
        "461 047",
        "461 048",
        "461 049",
        "461 050",
        "461 306",
        "461 051",
        "461 052",
        "461 053",
        "461 231",
        "461 311",
        "461 054",
        "461 055",
        "461 056",
        "461 057",
        "461 058",
        "461 059",
        "461 060",
        "461 061",
        "461 062",
        "461 204",
        "461 063",
        "461 064",
        "461 065",
        "461 066",
        "461 067",
        "461 304",
        "461 211",
        "461 171",
        "461 068",
        "461 225",
        "461 069",
        "461 166",
        "461 193",
        "461 070",
        "461 174",
        "461 173",
        "461 201",
        "461 179",
        "461 194",
        "461 071",
        "461 072",
        "461 073",
        "461 208",
        "461 074",
        "461 075",
        "461 185",
        "461 191",
        "461 076",
        "461 117",
        "461 118",
        "461 119",
        "461 120",
        "461 314",
        "461 121",
        "461 122",
        "461 123",
        "461 124",
        "461 125",
        "461 307",
        "461 126",
        "461 227",
        "461 192",
        "461 207",
        "461 214",
        "461 127",
        "461 128",
        "461 178",
        "461 077",
        "461 129",
        "461 130",
        "461 131",
        "461 133",
        "461 175",
        "461 321",
        "461 134",
        "461 222",
        "461 189",
        "461 135",
        "461 136",
        "461 300",
        "461 137",
        "461 213",
        "461 139",
        "461 140",
        "461 141",
        "461 142",
        "461 132",
        "461 319",
        "461 144",
        "461 312",
        "461 172",
        "461 148",
        "461 149",
        "461 181",
        "461 150",
        "461 215",
        "461 216",
        "461 151",
        "461 228",
        "461 152",
        "461 301",
        "461 183",
        "461 203",
        "461 164",
        "461 153",
        "461 163",
        "461 187",
        "461 154",
        "461 155",
        "461 156",
        "461 157",
        "461 182",
        "461 400",
    ]
    return zip_lists(get_expected_locations(), identifiers)


def get_expected_location_names():
    names = [
        "Bačický potok",
        "Baláš 1A",
        "Balinka 1",
        "Balinka 1A",
        "Balinka 1B",
        "Bílý potok 2A",
        "Blata 3",
        "Bobrava 1",
        "Bobrava 2",
        "Bobrava 2A",
        "Brodecký potok 1",
        "Brtnice 1",
        "Brtnice 1A",
        "Buchlovický potok 1",
        "Buchlovický potok 1M",
        "Bystřice Pernštejnská 2",
        "Býkovka 1A",
        "Cézava 1",
        "Cézava 1A",
        "Cézava 2",
        "Cézava 2A",
        "Cézava 3A",
        "Cikhájský potok 1",
        "Dřevnice 1",
        "Dřevnice 1A",
        "Dyje 2",
        "Dyje 3",
        "Dyje 3A",
        "Dyje 4",
        "Dyje 4A",
        "Dyje 4B",
        "Dyje 4C",
        "Dyje 4C/1",
        "Dyje 4D",
        "Dyje 4E",
        "Dyje 4G",
        "Dyje 4M",
        "Dyje 5",
        "Dyje 5A",
        "Dyje 7",
        "Dyje 7A",
        "Dyje 7B",
        "Dyje 8",
        "Dyje 9",
        "Dyje 10",
        "Dyje 11",
        "Dyje 11A",
        "Dyje 15",
        "Dyje 19",
        "Dyje 19A",
        "Dyje 19B",
        "Dyje 19C",
        "Grešlovomýtský potok 1",
        "Habrovanský potok 1A",
        "Haná 1",
        "Haná 1A",
        "Haná 1B",
        "Haná 2",
        "Haná 3",
        "Haná 3M",
        "Herdy",
        "Hloučela 1",
        "Malá Bečva 1",
        "Malá Bečva 1A",
        "Markovka 1",
        "Mocla 1",
        "Mocla 1M",
        "Mocla 2",
        "Morava 2",
        "Morava 3",
        "Morava 4",
        "Morava 4A",
        "Morava 4B",
        "Morava 4C",
        "Morava 5",
        "Morava 6",
        "Morava 6A",
        "Morava 6M",
        "Morava 7",
        "Morava 7A",
        "Morava 8",
        "Morava 8A",
        "Morava 9",
        "Morava 9A",
        "Morava 9B",
        "Morava 9C",
        "Morava 10",
        "Morava 10A",
        "Morava 11",
        "Morava 12",
        "Morava 12A",
        "Morava 12M",
        "Morava 13",
        "Morava 13A",
        "Morava 13B",
        "Morava 13C",
        "Myslůvka 1",
        "Myslůvka 1M",
        "Návesní rybník",
        "Okluka 1",
        "Olešnický potok 1A",
        "Olšava 1",
        "Olšava 1A",
        "Olšava 1B",
        "Olšava 2",
        "Olšava 2A",
        "Olšava 3A",
        "Oslava 1",
        "Oslava 1M",
        "Oslava 2",
        "Oslava 3",
        "Oslava 4",
        "Oslava 4M",
        "Oslava 5",
        "Oslava 6A",
        "Oslava 7",
        "Oslava 7A",
        "Oslava 8",
        "Pávov 1",
        "Podomský potok 1",
        "Podomský potok 1A",
        "Podomský potok 1B",
        "Prušánecký potok 1",
        "Chlumský potok 1A",
        "Ivanovický potok 1",
        "Januštice 1A",
        "Jaroměřice 1",
        "Jaroměřice 1A",
        "Jaroměřice 1B",
        "Jaroměřice 1M",
        "Jevišovka 1",
        "Jevišovka 1A",
        "Jevišovka 2",
        "Jevišovka 2A",
        "Jevišovka 3",
        "Jihlava 1",
        "Jihlava 1M",
        "Jihlava 2",
        "Jihlava 3",
        "Jihlava 4",
        "Jihlava 4A",
        "Jihlava 5M",
        "Jihlava 6",
        "Jihlava 6A",
        "Jihlava 7-8",
        "Jihlava 9",
        "Jihlava 10",
        "Jihlava 11",
        "Jihlava 12",
        "Jihlava 13",
        "Jihlava 13A",
        "Jihlava 13B",
        "Jihlava 13C",
        "Jihlava 14",
        "Jihlava 15",
        "Jihlava 15A",
        "Klimšák 1",
        "Klimšák 1M",
        "Kočkův rybník 1",
        "Kovalovický potok 1",
        "Křetínka 1",
        "Křovačka 1",
        "Kyjovka 2",
        "Kyjovka 2/1",
        "Kyjovka 2/2",
        "Kyjovka 2A",
        "Kyjovka 2B",
        "Kyjovka 2C",
        "Kyjovka 2C/1",
        "Kyjovka 2D",
        "Kyjovka 2E",
        "Kyjovka 3",
        "Kyjovka 3A",
        "Kyjovka 3B",
        "Kyjovka 3C",
        "Kyjovka 4A",
        "Líšeňská říčka 1",
        "Loučka 1A",
        "Loučka 4A",
        "Lubí 1",
        "Rakovec 1",
        "Rakovec 2",
        "Roketnice 1",
        "Rokytná 1",
        "Rokytná 1M",
        "Rokytná 2",
        "Rokytná 3",
        "Rokytná 3A",
        "Rokytná 4",
        "Rokytná 5",
        "Rokytná 5M",
        "Rokytná 6",
        "Rokytná 6A",
        "Romže 3A",
        "Romže 3C",
        "Romže 3D",
        "Rostěnický potok 1",
        "Rusava 2",
        "Rusava 2A",
        "Rusava 2B",
        "Sázava 17",
        "Sázava 18",
        "Sázava 19",
        "Stařečský potok 1",
        "Stařečský potok 1A",
        "Stařečský potok 1B",
        "Svitava 1",
        "Svitava 3A",
        "Svitava 5A",
        "Svratka 1",
        "Svratka 1A",
        "Svratka 1M",
        "Svratka 2",
        "Svratka 2B",
        "Svratka 3",
        "Svratka 4",
        "Svratka 5",
        "Svratka 6",
        "Svratka 7-8A",
        "Svratka 11M",
        "Svratka 14A",
        "Svratka 14M",
        "Ščávnice 2A",
        "Švábovský potok 1",
        "Trkmanka 1",
        "Trkmanka 2",
        "Třešťský potok 1",
        "Valcha 1",
        "Valcha 2",
        "Valová 2",
        "Vápovka 2",
        "Velička 1",
        "Velička 1M",
        "Velička 2",
        "Vícemilice 1",
        "Vlára 1",
        "Vlára 1A",
        "Vracov 1",
        "Žďárná 1",
        "Želetavka 1",
        "Želetavka 1A",
        "Želetavka 2",
        "Želetavka 2A",
        "Želetavka 2B",
        "Želetavka 2C",
    ]
    return zip_lists(get_expected_locations(), names)
