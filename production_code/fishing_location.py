class FishingLocation(object):
    def __init__(self, identifier, name, locations, headquarter, area):
        self.identifier = identifier
        self.name = name
        self.locations = locations
        self.headquarter = headquarter
        self.area = area

    def __str__(self):
        return self.identifier + ", " + self.name
