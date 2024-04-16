from typing import Optional

from src.behavioral.observer.enums import EventType
from src.behavioral.observer.publisher import EventManager


class WeatherStation:
    def __init__(self) -> None:
        self._temperature: Optional[float] = None
        self._wind_speed: Optional[float] = None
        self._pressure: Optional[float] = None
        self._humidity: Optional[float] = None
        self.event_manager: EventManager = EventManager()

    def set_temperature(self, new_temperature):
        self._temperature = new_temperature
        self.event_manager.notify(EventType.TEMPERATURE, new_temperature)

    def set_wind_speed(self, new_wind_speed):
        self._wind_speed = new_wind_speed
        self.event_manager.notify(EventType.WIND_SPEED, new_wind_speed)

    def set_pressure(self, new_pressure):
        self._pressure = new_pressure
        self.event_manager.notify(EventType.PRESSURE, new_pressure)

    def set_humidity(self, new_humidity):
        self._humidity = new_humidity
        self.event_manager.notify(EventType.HUMIDITY, new_humidity)

    def set_event_manager(self, event_manager: EventManager):
        self.event_manager = event_manager
