import abc

from src.behavioral.observer.enums import EventType


class EventListener(abc.ABC):
    """Interface of event listeners of the weather station."""

    @abc.abstractmethod
    def update(self, event_type: str, new_value: float) -> None:
        """Update the value of the attributes received.

        Implementations of this method should use the values passed
        through parameters to update the attributes of the concrete
        class.
        """
        pass


class UserInterface(EventListener):
    """Concrete class of the event listeners of the weather station."""

    def __init__(self) -> None:
        self._temperature = None
        self._humidity = None

    def update(self, event_type: str, new_value: float) -> None:
        """Update the value of the attributes received."""
        if event_type == "temperature":
            self._temperature = new_value
        elif event_type == EventType.HUMIDITY.value:
            self._humidity = new_value
        else:
            pass

    def display(self) -> str:
        """Display the updated information.

        Returns:
            str: Updated information for UI
        """
        return f"Temperature: {self._temperature}\n" f"Humidity: {self._humidity}\n"


class Logger(EventListener):
    """Concrete class of the event listeners of the weather station."""

    def __init__(self) -> None:
        self._temperature = None
        self._wind_speed = None
        self._pressure = None
        self._humidity = None

    def update(self, event_type: str, new_value: float) -> None:
        """Update the value of the attributes received."""
        if event_type == EventType.TEMPERATURE.value:
            self._temperature = new_value
        elif event_type == EventType.WIND_SPEED.value:
            self._wind_speed = new_value
        elif event_type == EventType.PRESSURE.value:
            self._pressure = new_value
        elif event_type == EventType.HUMIDITY.value:
            self._humidity = new_value
        else:
            pass

    def log(self) -> str:
        """Log the updated information.

        Returns:
            str: Updated information to log
        """
        return (
            f"[LOG] Temperature: {self._temperature}\n"
            f"[LOG] Wind Speed: {self._wind_speed}\n"
            f"[LOG] Pressure: {self._pressure}\n"
            f"[LOG] Humidity: {self._humidity}\n"
        )


class AlertSystem(EventListener):
    """Concrete class of the event listeners of the weather station."""

    def __init__(self) -> None:
        self._temperature = None
        self._wind_speed = None

    def update(self, event_type: str, new_value: float) -> None:
        """Update the value of the attributes received."""
        if event_type == EventType.TEMPERATURE.value:
            self._temperature = new_value
        elif event_type == EventType.WIND_SPEED.value:
            self._wind_speed = new_value
        else:
            pass

    def alert(self) -> str:
        """Return an alert with the updated information.

        Returns:
            str: Updated information to alert
        """
        return f"[ALERT] Temperature: {self._temperature}\n" f"[ALERT] Wind Speed: {self._wind_speed}\n"
