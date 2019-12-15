class FishingLocation(object):
    def __init__(self, identifier, name, locations, headquarter):
        self.identifier = identifier
        self.name = name
        self.locations = locations
        self.headquarter = headquarter

    def __str__(self):
        return self.identifier + ", " + self.name
