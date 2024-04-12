from src.structural.adapter import adapter, drones

drone = drones.SuperDrone()
drone_adapter = adapter.DroneAdapter(drone)


class TestSuperDroneAdapterQuack:
    def test_correct_type(self):
        actual = drone_adapter.quack()
        assert isinstance(actual, str), f"Wrong type. Expected 'str', got {type(actual)}"

    def test_correct_value(self):
        expected = "Beep beep beep"
        actual = drone_adapter.quack()
        assert expected == actual, f"Wrong value. Expected {expected} but got {actual}."


class TestSuperDroneAdapterFly:
    def test_correct_type(self):
        actual = drone_adapter.fly()
        assert isinstance(actual, str), f"Wrong type. Expected 'str', got {type(actual)}"

    def test_correct_value(self):
        expected = "Rotors are spinning\nTaking off"
        actual = drone_adapter.fly()
        assert expected == actual, f"Wrong value. Expected {expected} but got {actual}."
