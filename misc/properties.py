class Coordinate:
    def __init__(self, lat: float, long: float) -> None:
        self._latitude = self._longitude = 0.0
        self.latitude = lat
        self.longitude = long

    @property
    def latitude(self) -> float:
        return self._latitude

    @latitude.setter
    def latitude(self, lat_value: float) -> None:
        if not -90 <= lat_value <= 90:
            raise ValueError(f"{lat_value} is an invalid value for latitude")
        self._latitude = lat_value

    @property
    def longitude(self) -> float:
        return self._longitude

    @longitude.setter
    def longitude(self, long_value: float) -> None:
        if not -180 <= long_value <= 180:
            raise ValueError(f"{long_value} is an invalid value for longitude")
        self._longitude = long_value


def main() -> None:
    coordinate = Coordinate(45.45, 90.90)
    print(coordinate.longitude, coordinate.latitude)
    # coordinate.latitude = 91.9
    # coordinate.longitude = 191.1


if __name__ == "__main__":
    main()
