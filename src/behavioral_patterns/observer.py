import abc


class Observer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self, temperature: float, humidity: float, pressure: float):
        pass


class Subject(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def register_observer(self, observer: Observer):
        pass

    @abc.abstractmethod
    def remove_observer(self, observer: Observer):
        pass

    @abc.abstractmethod
    def notify_observers(self):
        pass


class DisplayElement(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def display(self):
        pass


class WeatherData(Subject):
    def __init__(self):
        self._observers = []
        self._temperature = None
        self._humidity = None
        self._pressure = None

    def register_observer(self, observer: Observer):
        self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temperature: float, humidity: float, pressure: float):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure

        self.measurements_changed()


class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data: WeatherData):
        self._temperature = None
        self._humidity = None
        self._pressure = None
        self._weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, temperature: float, humidity: float, pressure: float):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure

    def display(self):
        print("Current conditions: {} F degrees and {}% humidity. Pressure: {}".format(
            self._temperature, self._humidity, self._pressure)
        )


def main():
    weather_data = WeatherData()
    conditions_display = CurrentConditionsDisplay(weather_data)
    conditions_display.display()

    weather_data.set_measurements(47.34, 38.6, 12.34)
    conditions_display.display()


if __name__ == "__main__":
    main()