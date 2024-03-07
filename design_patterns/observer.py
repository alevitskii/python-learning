from typing import Protocol


class Observable(Protocol):
    def update(self) -> None: ...


class DisplayableAndObservable(Observable, Protocol):
    def display(self) -> None: ...


class SubjectProtocol(Protocol):
    def register_observer(self, o: DisplayableAndObservable) -> None: ...

    def unregister_observer(self, o: DisplayableAndObservable) -> None: ...

    def notify_observers(self) -> None: ...


class WeatherData:
    def __init__(self) -> None:
        self._temperature: float = 0
        self._humidity: float = 0
        self._pressure: float = 0
        self._observers: list[DisplayableAndObservable] = []

    @property
    def temperature(self) -> float:
        return self._temperature

    @property
    def humidity(self) -> float:
        return self._humidity

    @property
    def pressure(self) -> float:
        return self._pressure

    def register_observer(self, o: DisplayableAndObservable) -> None:
        self._observers.append(o)

    def unregister_observer(self, o: DisplayableAndObservable) -> None:
        self._observers.remove(o)

    def notify_observers(self) -> None:
        for o in self._observers:
            o.update()

    def measurements_changed(self) -> None:
        self.notify_observers()

    def set_measurements(self, temperature: float, humidity: float, pressure: float) -> None:
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.measurements_changed()


class ForecastDisplay:
    def __init__(self, weather_data: WeatherData) -> None:
        self._current_pressure = self._last_pressure = 29.92
        self._weather_data = weather_data
        # it's not necessary to register here
        weather_data.register_observer(self)

    def update(self) -> None:
        self._last_pressure = self._current_pressure
        self._current_pressure = self._weather_data.pressure
        self.display()

    def display(self) -> None:
        if self._current_pressure > self._last_pressure:
            print("Improving weather on the way!")
        elif self._current_pressure == self._last_pressure:
            print("More of the same")
        elif self._current_pressure < self._last_pressure:
            print("Watch out for cooler, rainy weather")


class CurrentConditionsDisplay:
    def __init__(self, weather_data: WeatherData) -> None:
        self._temperature = 0
        self._humidity = 0
        self._weather_data = weather_data
        weather_data.register_observer(self)

    def update(self) -> None:
        self._temperature = self._weather_data.temperature
        self._humidity = self._weather_data.humidity
        self.display()

    def display(self) -> None:
        print(f"Current conditions: {self._temperature}F degrees and {self._humidity}% humidity")


class StatisticsDisplay:
    def __init__(self, weather_data: WeatherData) -> None:
        self._max_temp = 0
        self._min_temp = 200
        self._temp_sum = 0
        self._num_readings = 0
        self._weather_data = weather_data
        weather_data.register_observer(self)

    def update(self) -> None:
        self._temp_sum += self._weather_data.temperature
        self._num_readings += 1

        if self._weather_data.temperature > self._max_temp:
            self._max_temp = self._weather_data.temperature
        elif self._weather_data.temperature < self._min_temp:
            self._min_temp = self._weather_data.temperature

        self.display()

    def display(self) -> None:
        print(f"Avg/Max/Min temperature = {self._temp_sum / self._num_readings}/{self._max_temp}/{self._min_temp}")


def compute_heat_index(t: float, rh: float):
    return (
        16.923
        + (0.185212 * t)
        + (5.37941 * rh)
        - (0.100254 * t * rh)
        + (0.00941695 * (t * t))
        + (0.00728898 * (rh * rh))
        + (0.000345372 * (t * t * rh))
        - (0.000814971 * (t * rh * rh))
        + (0.0000102102 * (t * t * rh * rh))
        - (0.000038646 * (t * t * t))
        + (0.0000291583 * (rh * rh * rh))
        + (0.00000142721 * (t * t * t * rh))
        + (0.000000197483 * (t * rh * rh * rh))
        - (0.0000000218429 * (t * t * t * rh * rh))
        + 0.000000000843296 * (t * t * rh * rh * rh)
    ) - (0.0000000000481975 * (t * t * t * rh * rh * rh))


class HeatIndexDisplay:
    def __init__(self, weather_data: WeatherData) -> None:
        self._heat_index = 0
        self._weather_data = weather_data
        weather_data.register_observer(self)

    def update(self):
        self._heat_index = compute_heat_index(t=self._weather_data.temperature, rh=self._weather_data.humidity)
        self.display()

    def display(self):
        print(f"Heat index is: {self._heat_index}")


def main() -> None:
    weather_data = WeatherData()
    _ = CurrentConditionsDisplay(weather_data=weather_data)
    _ = ForecastDisplay(weather_data=weather_data)
    _ = HeatIndexDisplay(weather_data=weather_data)
    statistics_display = StatisticsDisplay(weather_data=weather_data)
    weather_data.set_measurements(temperature=80, humidity=65, pressure=30.4)
    weather_data.set_measurements(temperature=82, humidity=70, pressure=29.2)
    weather_data.unregister_observer(statistics_display)
    weather_data.set_measurements(temperature=78, humidity=90, pressure=29.2)


if __name__ == "__main__":
    main()
