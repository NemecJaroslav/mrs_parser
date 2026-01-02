from production_code.common.constants import Constants


class MRSConstants:
    GPS_PATTERN = r'(?:\bGPS\b[^0-9NSnsEWew]+?)?'\
                  r'(?P<lat>\d{1,2}(?:\.\d+)?)\s*(?P<lat_hemi>[NSns])\s*,\s*'\
                  r'(?P<lon>\d{1,3}(?:\.\d+)?)\s*(?P<lon_hemi>[EWew])'\
                  r'(?=(?:\s*[,;]|$|[^0-9NSnsEWew]+))'
