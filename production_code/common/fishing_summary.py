from production_code.common.constants import Constants


class FishingSummary(object):
    def __init__(self, identifier, name, visits_count):
        self.identifier = identifier
        self.name = name
        self.visits_count = visits_count

    def __str__(self):
        return (str(self.identifier) + Constants.SPACE
                + str(self.name) + Constants.SPACE
                + str(self.visits_count) + Constants.TIMES)
