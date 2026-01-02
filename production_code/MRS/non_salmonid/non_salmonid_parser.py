from production_code.MRS.common.mrs_parser import MRSParser
from .constants import NonSalmonidConstants
from .justified_close_locations import justified_close_locations


class NonSalmonidParser(MRSParser):
    @staticmethod
    def get_parser_description():
        return "MRS (mimopstruhove)"

    def _get_justified_close_locations(self):
        return justified_close_locations

    def _get_incorrect_gps(self):
        return NonSalmonidConstants.INCORRECT_GPS

    def _get_headquarter_gps(self, headquarter):
        return NonSalmonidConstants.HEADQUARTER_GPS[headquarter]

    def get_url_to_bpvr(self):
        file_id = "18WmpnlBkfeCD_79biAVpxiUHeLfweRKC"
        return f"https://drive.google.com/uc?export=download&id={file_id}"

    def get_phase_in_bpvr_to_look_for(self):
        return "REVÍRY MIMOPSTRUHOVÉ"

    def get_location_id_start(self):
        return "461"
