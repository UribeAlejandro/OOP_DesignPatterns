from typing import Dict, List

from src.behavioral.observer.enums import EventType
from src.behavioral.observer.subscribers import EventListener


class EventManager:
    """Notifies updates to subscribed listeners to each event type."""

    def __init__(self) -> None:
        self.listeners: Dict[str, List[EventListener]] = {
            EventType.TEMPERATURE.value: [],
            EventType.WIND_SPEED.value: [],
            EventType.PRESSURE.value: [],
            EventType.HUMIDITY.value: [],
        }

    def subscribe(self, event_type: EventType, listener: EventListener) -> None:
        """Subscribes a listener to the given event type.

        Args:
            event_type (EventType): Event type to be subscribed to
            listener (EventListener): Listener to be
            subscribed to the given event type
        """
        self.listeners[event_type.value] += [listener]

    def notify(self, event_type: EventType, data: float) -> None:
        """Notify the updated data to appropriate subscribed listeners.

        Args:
            event_type (EventType): Event type that is updated
            data (float): Updated data for the given event type
        """
        listeners_ = self.listeners[event_type.value]
        for listener in listeners_:
            listener.update(event_type.value, data)
