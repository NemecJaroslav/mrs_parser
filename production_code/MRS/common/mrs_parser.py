import requests
from pypdf import PdfReader
from io import BytesIO
from typing import List, Tuple
import re
from production_code.common.gps_coordinate import DDComponent
from production_code.common.parser import Parser
from production_code.MRS.common.constants import MRSConstants
from production_code.common.fishing_location import FishingLocation


class MRSParser(Parser):
    @staticmethod
    def _get_bpvr():
        FILE_ID = "18WmpnlBkfeCD_79biAVpxiUHeLfweRKC"
        URL = f"https://drive.google.com/uc?export=download&id={FILE_ID}"
        PHRASE = "REVÍRY MIMOPSTRUHOVÉ"

        # stáhnout PDF do paměti
        r = requests.get(URL)
        r.raise_for_status()
        reader = PdfReader(BytesIO(r.content))

        # spojit text všech stran
        all_text = []
        for page in reader.pages:
            all_text.append(page.extract_text() or "")
        joined = "\n".join(all_text)

        # najít frázi a vrátit text od ní dál
        idx = joined.find(PHRASE)
        if idx == -1:
            return ""
        result = joined[idx+len(PHRASE):]
        return result

    @staticmethod
    def _get_locations(bpvr):
        lines = bpvr.splitlines()
        chunks = []
        current = []

        def flush():
            if current:
                chunks.append("\n".join(current).strip())
                current.clear()

        for line in lines:
            if line.startswith("461"):
                flush()
                current.append(line)  # zahrne i řádek "461..." do oddílu
            else:
                current.append(line)
        flush()
        return [c for c in chunks if c]

    @staticmethod
    def parse_gps(gps: str) -> List[Tuple[DDComponent, DDComponent]]:
        gps = gps.replace('\u00A0', ' ')  # normalize non-breaking spaces
        GPS_PATTERN = re.compile(
            r'(?:\bGPS\b[^0-9NSnsEWew]+?)?'  # optional "GPS ..." label
            r'(?P<lat>\d{1,2}(?:\.\d+)?)\s*(?P<lat_hemi>[NSns])\s*,\s*'
            r'(?P<lon>\d{1,3}(?:\.\d+)?)\s*(?P<lon_hemi>[EWew])\b'
        )
        results: List[Tuple[DDComponent, DDComponent]] = []
        for m in GPS_PATTERN.finditer(gps):
            lat_val = float(m.group('lat'))
            lon_val = float(m.group('lon'))
            lat_dir = m.group('lat_hemi').upper()
            lon_dir = m.group('lon_hemi').upper()

            lat_comp = DDComponent(lat_val, lat_dir)
            lon_comp = DDComponent(lon_val, lon_dir)
            results.append((lat_comp, lon_comp))
        return results

    def _get_locations_url(self):
        return self._get_locations(self._get_bpvr())

    def _get_decoded_source_page(self, location_url):
        return location_url

    def get_fishing_location(self, location):
        line = location.splitlines()[0]
        m_revir = re.search(r'(?P<cislo>\b461\s*\d{3}\b)', line)
        cislo_reviru = m_revir.group('cislo').replace(" ", "") if m_revir else None  # "461024"
        m_nazev = re.search(
            r'\b461\s*\d{3}\b\s+(?P<nazev>.+?)(?=\s*[-–—]+\s*(?:PS|MRS)\b)',
            line
        )
        nazev_reviru = m_nazev.group('nazev').strip().upper() if m_nazev else None  # "DYJE 5 – Novomlýnská nádrž"
        m_spolek = re.search(
            r'(?P<spolek>(?:PS|MRS)\b.+?)'
            r'(?=\s+\d+(?:[.,]\d+)?\s*(?:km|ha)\b|[,;|]|$)',
            line,
            flags=re.IGNORECASE
        )
        pobocny_spolek = re.sub(r'\s+', ' ', re.sub(r'^(?i:(PS))\s+', '',
                                                    m_spolek.group('spolek').replace('\u00A0', ' ')
                                                    .strip())).strip().upper() if m_spolek else None
        m_ha_all = re.findall(r'\b(?P<ha>\d{1,3}(?:[\s\u00A0]\d{3})*(?:[.,]\d+)?|\d+(?:[.,]\d+)?)\s*ha\b', line,
                              flags=re.IGNORECASE)
        vymera_ha = 0.0
        if m_ha_all:
            raw = m_ha_all[-1]  # pokud by se vyskytlo více "ha", bereme poslední
            vymera_ha = float(raw.replace(" ", "").replace("\u00A0", "").replace(",", "."))

        fishing_location = FishingLocation(
            cislo_reviru,
            nazev_reviru,
            pobocny_spolek,
            vymera_ha,
            self.parse_gps(location)
        )
        return fishing_location
