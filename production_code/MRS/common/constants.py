class Constants(object):
    MRS_HOME_PAGE = "http://www.mrsbrno.cz"
    LOCATION_URL_PATTERN_GROUP_NAME = "location_url"
    LOCATION_ID_PATTERN_GROUP_NAME = "location_id"
    LOCATION_ID_PATTERN = ("ev. číslo revíru:.*?(?P<"
                           + LOCATION_ID_PATTERN_GROUP_NAME
                           + ">\\d{3}\\s*\\d{3})<")
    LOCATION_NAME_PATTERN_GROUP_NAME = "location_name"
    LOCATION_NAME_PATTERN = ("<title>(?P<"
                             + LOCATION_NAME_PATTERN_GROUP_NAME
                             + ">.*?)</title>")
    HEADQUARTER_PATTERN_GROUP_NAME = "headquarter"
    HEADQUARTER_PATTERN = "hospodařením:.*?>" \
                          "(?P<" + HEADQUARTER_PATTERN_GROUP_NAME\
                          + ">[a-zA-z0-9ÁČĎÉĚÍŇÓŘŠŤÚŮÝŽáčďéěíňóřšťúůýž]" \
                          "[a-zA-z0-9ÁČĎÉĚÍŇÓŘŠŤÚŮÝŽáčďéěíňóřšťúůýž\\s.,-]+)"
    AREA_PATTERN_GROUP_NAME = "area"
    AREA_PATTERN = "výměra:.*?(?P<"\
                   + AREA_PATTERN_GROUP_NAME\
                   + ">[0-9][0-9,\\s]*)\\s+ha"
    UTF8 = "utf-8"
