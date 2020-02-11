from production_code.common.constants import Constants


class GPSCoordinate(object):
    def __init__(self, degrees, minutes, seconds, direction):
        self.degrees = degrees
        self.minutes = minutes
        self.seconds = seconds
        self.direction = direction

    def __eq__(self, other):
        if isinstance(other, GPSCoordinate):
            return (self.degrees == other.degrees
                    and self.minutes == other.minutes
                    and self.seconds == other.seconds
                    and self.direction == other.direction)
        return False

    def __str__(self):
        return (str(self.degrees)
                + Constants.COMMA + str(self.minutes)
                + Constants.COMMA + str(self.seconds)
                + Constants.COMMA + self.direction)
