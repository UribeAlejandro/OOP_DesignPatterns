from src.structural.decorator import doughs

neapolitan_pizza = doughs.NeapolitanPizza(doughs.PizzaSize.EXTRA_LARGE)


class TestGetSize:
    def test_correct_type(self):
        actual = neapolitan_pizza.get_size()
        assert isinstance(actual, doughs.PizzaSize), f"Wrong type. Expected 'str', got {type(actual)}"

    def test_correct_value(self):
        actual = neapolitan_pizza.get_size()
        expected = doughs.PizzaSize.EXTRA_LARGE
        assert expected == actual, f"Wrong value. Expected {expected} but got {actual}."


class TestGetDescription:
    def test_correct_type(self):
        actual = neapolitan_pizza.get_description()
        assert isinstance(actual, str), f"Wrong type. Expected 'str', got {type(actual)}"

    def test_correct_value(self):
        actual = neapolitan_pizza.get_description()
        expected = "Extra large Neapolitan style pizza"
        assert expected == actual, f"Wrong value. Expected {expected} but got {actual}."


class TestGetCost:
    def test_correct_type(self):
        actual = neapolitan_pizza.get_cost()
        assert isinstance(actual, float), f"Wrong type. Expected 'float', got {type(actual)}"

    def test_correct_value(self):
        actual = neapolitan_pizza.get_cost()
        expected = 24.0
        assert expected == actual, f"Wrong value. Expected {expected} but got {actual}."
