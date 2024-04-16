import enum


class EventType(str, enum.Enum):
    TEMPERATURE = "temperature"
    WIND_SPEED = "wind_speed"
    PRESSURE = "pressure"
    HUMIDITY = "humidity"
