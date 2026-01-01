from production_code.common.constants import Constants


class DDComponent:
    def __init__(self, value: float, direction: str):
        direction = direction.upper()
        if direction not in ("N", "S", "E", "W"):
            raise ValueError(f"Invalid direction: {direction}")
        if direction in ("N", "S") and not (-90 <= value <= 90):
            raise ValueError(f"Invalid latitude value: {value}")
        if direction in ("E", "W") and not (-180 <= value <= 180):
            raise ValueError(f"Invalid longitude value: {value}")
        self.value = float(value)
        self.direction = direction

    def convert_to_dd(self) -> float:
        sign = -1 if self.direction in ("S", "W") else 1
        return sign * self.value

    def __repr__(self):
        return f"DDComponent(value={self.value}, dir='{self.direction}')"

    def __eq__(self, other):
        if not isinstance(other, DDComponent):
            return False
        return (
            self.direction == other.direction and
            abs(self.value - other.value) < 1e-9
        )


class GPSCoordinate:
    def __init__(self, degrees, minutes, seconds, direction):
        self.degrees = degrees
        self.minutes = minutes
        self.seconds = seconds
        self.direction = direction

    def convert_to_dd(self):
        gps_in_dd = (self.degrees
                     + self.minutes / Constants.MINUTES_IN_HOUR
                     + self.seconds / Constants.SECONDS_IN_HOUR)
        if (self.direction == Constants.WEST
                or self.direction == Constants.SOUTH):
            return -gps_in_dd
        return gps_in_dd

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
