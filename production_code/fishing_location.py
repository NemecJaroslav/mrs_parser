class FishingLocation(object):
    def __init__(self, identifier, name, headquarter, area, gps_locations):
        self.identifier = identifier
        self.name = name
        self.headquarter = headquarter
        self.area = area
        self.gps_locations = gps_locations

    def __str__(self):
        return self.identifier + ", " + self.name
