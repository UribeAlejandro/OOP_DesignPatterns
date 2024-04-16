# Observer Pattern

The observer pattern is a behavioral design pattern that defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

## Problem

You are working on a `WeatherStation` class that records data from sensors from a weather station. You are building a web application that listens to events, and updates the `temperature`, `wind_speed`, `pressure` and `humidity` parameters according to the values sensed by the weather station. It then outputs the new values in different formats, visually through the `UserInterface` class, in the form of logs through the `Logger` class and as alerts thanks to the `AlertSystem` class.

Implement the Observer pattern to satisfy the functional requirement described above and make sure that your solution is easily extensible for other subscribers.

```mermaid
classDiagram
class WeatherStation {
    -temperature: float
    -wind_speed: float
    -pressure: float
    -humidity: foat
    +set_temperature()
    +set_wind_speed()
    +set_pressure()
    +set_humidity()
}
class UserInterface {
    -temperature: float
    -humidity: foat
    +update(event_type, new_value)
    +display() str
}
class Logger {
    -temperature: float
    -wind_speed: float
    -pressure: float
    -humidity: foat
    +update(event_type, new_value)
    +log() str
}
class AlertSystem {
    -temperature: float
    -wind_speed: float
    +update(event_type, new_value)
    +alert() str
}
class EventType{
    <<enumeration>>
    TEMPERATURE
    WIND_SPEED
    PRESSURE
    HUMIDITY
}
WeatherStation --> EventType
UserInterface --> EventType
Logger --> EventType
AlertSystem --> EventType
```

## Solution

In order to implement, let's define an *Observable* class. The *Observable* class is the one that changes its attributes from time to time. In this case, such class is the *WeatherStation* classs.

```mermaid
classDiagram
class WeatherStation {
    -temperature: float
    -wind_speed: float
    -pressure: float
    -humidity: foat
    +set_temperature()
    +set_wind_speed()
    +set_pressure()
    +set_humidity()
}
```

Let's define the *Subject* Interface, that we will call *EventManager*. This Interface has the attiribute *listeners*, which has a list of *EvenetListener* instances subscribed to each EventType. On the other hand, it might have the `notify()` and `subscribe()` methods, as follows:

```mermaid
classDiagram
class EventManager {
    +listeners: Dict[EventType, List[EventListener]]
    +subscribe()
    +notify()
}
```

Also, let's define the *Observer* Interface, that we will call *EventListener*. On the other hand, it might have the `update()` method, as follows:

```mermaid
classDiagram
class EventListener {
    +update()
}

class UserInterface {
    -temperature: float
    -humidity: float
    +update()
    +display()
}

class Logger {
    -temperature: float
    -wind_speed: float
    -pressure: float
    -humidity: float
    +update()
    +log()
}

class AlertSystem {
    -temperature: float
    -wind_speed: float
    +update()
    +alert()
}

UserInterface --> EventListener
Logger --> EventListener
AlertSystem --> EventListener
```

The *WeatherStation* class either implements or has a relationship by composition with the *EventManager*. The problem at hand uses composition. Then the *WeatherStation* class might include an attribute of type *EventManager* as follows:

```mermaid
classDiagram
class WeatherStation {
    -temperature: float
    -wind_speed: float
    -pressure: float
    -humidity: foat
    +event_manager: EventManager = new EventManager()
    +set_temperature()
    +set_wind_speed()
    +set_pressure()
    +set_humidity()
}
```

The instance of *event_manager* in the *WeatherStatuion* will be in charge of notifying all the subscribed observers in the *listeners* attribute in *EventManager* class. Then the relationship between *WeatherStation* and *EventManager* should look as follows:

```mermaid
classDiagram
class WeatherStation {
    -temperature: float
    -wind_speed: float
    -pressure: float
    -humidity: foat
    +event_manager: EventManager = new EventManager()
    +set_temperature()
    +set_wind_speed()
    +set_pressure()
    +set_humidity()
    +set_event_manager()
}

class EventManager {
    +listeners: Dict[EventType, List[EventListener]]
    +subscribe()
    +notify()
}

EventManager --* WeatherStation
```

Inside the methods `set_temperature()` `set_wind_speed()` `set_pressure()` & `set_humidity()` the attribute *event_manager* notifies observers, for example:

```python
def set_temperature(self, new_value):
    self._temperature = new_value
    self.event_manager.notify(EventType.TEMPERATURE, new_value)
```

Then the WeatherStation App looks as follows:

```mermaid
classDiagram
class WeatherStation {
    -temperature: float
    -wind_speed: float
    -pressure: float
    -humidity: foat
    +event_manager: EventManager = new EventManager()
    +set_temperature()
    +set_wind_speed()
    +set_pressure()
    +set_humidity()
    +set_event_manager()
}

class EventManager {
    +listeners: Dict[EventType, List[EventListener]]
    +subscribe()
    +notify()
}

class EventListener {
    +update()
}

class UserInterface {
    -temperature: float
    -humidity: float
    +update()
    +display()
}

class Logger {
    -temperature: float
    -wind_speed: float
    -pressure: float
    -humidity: float
    +update()
    +log()
}

class AlertSystem {
    -temperature: float
    -wind_speed: float
    +update()
    +alert()
}

class EventType{
    <<enumeration>>
    TEMPERATURE
    WIND_SPEED
    PRESSURE
    HUMIDITY
}


EventManager --* WeatherStation : composition
UserInterface --|> EventListener : implements
Logger --|> EventListener : implements
AlertSystem --|> EventListener : implements
EventListener --o EventManager : aggregation
WeatherStation --> EventType : association
UserInterface --> EventType : association
Logger --> EventType : association
AlertSystem --> EventType : association
```
