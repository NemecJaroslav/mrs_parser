class FishingLocation(object):
    def __init__(self, identifier, name, locations, headquarters):
        self.identifier = identifier
        self.name = name
        self.locations = locations
        self.headquarters = headquarters

    def __str__(self):
        return self.identifier + ", " + self.name
