class FishingLocation(object):
    def __init__(self, identifier, name, locations):
        self.identifier = identifier
        self.name = name
        self.locations = locations

    def __str__(self):
        return self.identifier + ", " + self.name
