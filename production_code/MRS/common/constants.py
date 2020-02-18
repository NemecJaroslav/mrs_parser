from production_code.common.constants import Constants


class MRSConstants(object):
    MRS_HOME_PAGE = "http://www.mrsbrno.cz"
    LOCATION_ID_PATTERN = ("ev. číslo revíru:.*?(?P<"
                           + Constants.LOCATION_ID_PATTERN_GROUP_NAME
                           + ">\\d{3}\\s*\\d{3})<")
    LOCATION_NAME_PATTERN = ("<title>(?P<"
                             + Constants.LOCATION_NAME_PATTERN_GROUP_NAME
                             + ">.*?)</title>")
    HEADQUARTER_PATTERN = "hospodařením:.*?>" \
                          "(?P<" + Constants.HEADQUARTER_PATTERN_GROUP_NAME\
                          + ">[a-zA-z0-9ÁČĎÉĚÍŇÓŘŠŤÚŮÝŽáčďéěíňóřšťúůýž]" \
                          "[a-zA-z0-9ÁČĎÉĚÍŇÓŘŠŤÚŮÝŽáčďéěíňóřšťúůýž\\s.,-]+)"
    AREA_PATTERN = "výměra:.*?(?P<"\
                   + Constants.AREA_PATTERN_GROUP_NAME\
                   + ">[0-9][0-9,\\s]*)\\s+ha"
