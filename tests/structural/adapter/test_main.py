from src.structural.adapter import adapter, drones, ducks, main

duck_simulator = main.DuckSimulator()
mallard_duck = ducks.MallardDuck()
drone = drones.SuperDrone()
drone_adapter = adapter.DroneAdapter(drone)


class TestSimulateMallardDuck:
    def test_correct_type(self):
        actual = duck_simulator.simulate_duck(mallard_duck)
        assert isinstance(actual, str), f"Wrong type. Expected 'str', got {type(actual)}"

    def test_correct_value(self):
        expected = "quack quackkkk!!\nFlying like a Mallard Duck"
        actual = duck_simulator.simulate_duck(mallard_duck)
        assert expected == actual, f"Wrong value. Expected {expected} but got {actual}."


class TestSimulateDroneAdapter:
    def test_correct_type(self):
        actual = duck_simulator.simulate_duck(drone_adapter)
        assert isinstance(actual, str), f"Wrong type. Expected 'str', got {type(actual)}"

    def test_correct_value(self):
        expected = "Beep beep beep\nRotors are spinning\nTaking off"
        actual = duck_simulator.simulate_duck(drone_adapter)
        assert expected == actual, f"Wrong value. Expected {expected} but got {actual}."
