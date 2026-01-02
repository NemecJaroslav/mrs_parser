import requests
from pypdf import PdfReader
from io import BytesIO
from typing import List, Tuple
import re
from production_code.common.gps_coordinate import DDComponent
from production_code.common.parser import Parser
from production_code.common.constants import Constants
from production_code.MRS.common.constants import MRSConstants
from production_code.common.fishing_location import FishingLocation


class MRSParser(Parser):
    def _get_justified_close_locations(self):
        raise NotImplementedError("Must be implemented")

    def _get_locations(self):
        return self._get_fishing_locations(self._get_raw_fishing_locations())

    def _get_incorrect_gps(self):
        raise NotImplementedError("Must be implemented")

    def _get_headquarter_gps(self, headquarter):
        raise NotImplementedError("Must be implemented")

    @staticmethod
    def get_parser_description():
        raise NotImplementedError("Must be implemented")

    # No decoding done as we parse PDF file in case of MRS
    def _get_decoded_source_page(self, location_url):
        return location_url

    def get_url_to_bpvr(self):
        raise NotImplementedError("Must be implemented")

    def get_phase_in_bpvr_to_look_for(self):
        raise NotImplementedError("Must be implemented")

    def get_location_id_start(self):
        raise NotImplementedError("Must be implemented")

    def _get_raw_fishing_locations(self):
        r = requests.get(self.get_url_to_bpvr())
        r.raise_for_status()
        reader = PdfReader(BytesIO(r.content))

        all_text = []
        for page in reader.pages:
            all_text.append(page.extract_text() or Constants.EMPTY_STRING)
        joined = Constants.NEW_LINE.join(all_text)

        phrase = self.get_phase_in_bpvr_to_look_for()
        idx = joined.find(phrase)
        if idx == -1:
            return Constants.EMPTY_STRING
        result = joined[idx+len(phrase):]
        return result

    def _get_fishing_locations(self, bpvr):
        lines = bpvr.splitlines()
        chunks = []
        current = []

        def flush():
            if current:
                chunks.append(Constants.NEW_LINE.join(current).strip())
                current.clear()

        for line in lines:
            if line.startswith(self.get_location_id_start()):
                flush()
                current.append(line)
            else:
                current.append(line)
        flush()
        return [c for c in chunks if c]

    @staticmethod
    def parse_gps(gps: str) -> List[Tuple[DDComponent, DDComponent]]:
        gps = gps.replace('\u00A0', ' ')
        gps_pattern = re.compile(MRSConstants.GPS_PATTERN)
        results: List[Tuple[DDComponent, DDComponent]] = []
        for m in gps_pattern.finditer(gps):
            lat_val = float(m.group('lat'))
            lon_val = float(m.group('lon'))
            lat_dir = m.group('lat_hemi').upper()
            lon_dir = m.group('lon_hemi').upper()

            lat_comp = DDComponent(lat_val, lat_dir)
            lon_comp = DDComponent(lon_val, lon_dir)
            results.append((lat_comp, lon_comp))
        return results

    def _get_identifier(self, line):
        prefix = re.escape(self.get_location_id_start())
        pattern = rf'(?P<identifier>\b{prefix}\s*\d{{3}}\b)'
        m_identifier = re.search(pattern, line)
        identifier = m_identifier.group('identifier').replace(" ", "") if m_identifier else None
        return identifier

    def _get_name(self, line):
        m_name = re.search(
            rf'\b{re.escape(self.get_location_id_start())}\s*\d{{3}}\b\s+(?P<name>.+?)(?=\s*[-–—]+\s*(?:PS|MRS)\b)',
            line
        )
        name = m_name.group('name').strip().upper() if m_name else None
        return name

    @staticmethod
    def __get_headquarter(line):
        m_headquarter = re.search(
            r'(?P<headquarter>(?:PS|MRS)\b.+?)'
            r'(?=\s+\d+(?:[.,]\d+)?\s*(?:km|ha)\b|[,;|]|$)',
            line,
            flags=re.IGNORECASE
        )
        headquarter = re.sub(r'\s+', ' ', re.sub(r'^(?i:(PS))\s+', '',
                                                 m_headquarter.group('headquarter').replace('\u00A0', ' ')
                                                 .strip())).strip().upper() if m_headquarter else None
        return headquarter

    @staticmethod
    def __get_area(line):
        m_area = re.findall(r'\b(?P<area>\d{1,3}(?:[\s\u00A0]\d{3})*(?:[.,]\d+)?|\d+(?:[.,]\d+)?)\s*ha\b', line,
                            flags=re.IGNORECASE)
        area = 0.0
        if m_area:
            raw = m_area[-1]
            area = float(raw.replace(" ", "").replace("\u00A0", "").replace(",", "."))
        return area

    def get_fishing_location(self, location):
        line = location.splitlines()[0]
        fishing_location = FishingLocation(
            self._get_identifier(line),
            self._get_name(line),
            self.__get_headquarter(line),
            self.__get_area(line),
            self.parse_gps(location)
        )
        return fishing_location
