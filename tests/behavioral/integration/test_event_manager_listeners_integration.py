from src.behavioral.observer import publisher, subscribers
from src.behavioral.observer.enums import EventType

event = publisher.EventManager()
user_interface = subscribers.UserInterface()
logger = subscribers.Logger()
alert_system = subscribers.AlertSystem()

event.subscribe(EventType.TEMPERATURE, user_interface)
event.subscribe(EventType.TEMPERATURE, logger)
event.subscribe(EventType.TEMPERATURE, alert_system)
event.notify(EventType.TEMPERATURE, 21.0)

event.subscribe(EventType.WIND_SPEED, logger)
event.subscribe(EventType.WIND_SPEED, alert_system)
event.notify(EventType.WIND_SPEED, 3.5)

event.subscribe(EventType.PRESSURE, logger)
event.notify(EventType.PRESSURE, 100.1)

event.subscribe(EventType.HUMIDITY, user_interface)
event.subscribe(EventType.HUMIDITY, logger)
event.notify(EventType.HUMIDITY, 21.0)


class TestSubscribe:
    def test_subscribe_to_temperature_event(self):
        subs_list = event.listeners[EventType.TEMPERATURE.value]
        assert len(subs_list) == 3, f"Wrong value. Expected {3} but got {subs_list}."

    def test_subscribe_to_wind_speed_event(self):
        subs_list = event.listeners[EventType.WIND_SPEED.value]
        assert len(subs_list) == 2, f"Wrong value. Expected {2} but got {subs_list}."

    def test_subscribe_to_pressure_event(self):
        subs_list = event.listeners[EventType.PRESSURE.value]
        assert len(subs_list) == 1, f"Wrong value. Expected {1} but got {subs_list}."

    def test_subscribe_to_humidity_event(self):
        subs_list = event.listeners[EventType.WIND_SPEED.value]
        assert len(subs_list) == 2, f"Wrong value. Expected {2} but got {subs_list}."


class TestNotifyTemperatureEvent:
    def test_correct_value(self):
        expected = 21.0
        actual_user_interface = user_interface._temperature
        actual_logger = logger._temperature
        actual_alert_system = alert_system._temperature

        assert expected == actual_user_interface, f"Wrong value. Expected {expected} but got {actual_user_interface}."
        assert expected == actual_logger, f"Wrong value. Expected {expected} but got {actual_logger}."
        assert expected == actual_alert_system, f"Wrong value. Expected {expected} but got {actual_alert_system}."


class TestNotifyWindSpeedEvent:
    def test_correct_value(self):
        expected = 3.5
        actual_logger = logger._wind_speed
        actual_alert_system = alert_system._wind_speed

        assert expected == actual_logger, f"Wrong value. Expected {expected} but got {actual_logger}."
        assert expected == actual_alert_system, f"Wrong value. Expected {expected} but got {actual_alert_system}."


class TestNotifyPressureEvent:
    def test_correct_value(self):
        expected = 100.1
        actual_logger = logger._pressure

        assert expected == actual_logger, f"Wrong value. Expected {expected} but got {actual_logger}."


class TestNotifyHumidityEvent:
    def test_correct_value(self):
        expected = 21.0
        actual_user_interface = user_interface._humidity
        actual_logger = logger._humidity

        assert expected == actual_user_interface, f"Wrong value. Expected {expected} but got {actual_user_interface}."
        assert expected == actual_logger, f"Wrong value. Expected {expected} but got {actual_logger}."
