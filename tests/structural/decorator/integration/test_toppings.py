from src.structural.decorator import doughs, toppings

neapolitan_pizza = doughs.NeapolitanPizza(doughs.PizzaSize.EXTRA_LARGE)

marinara_neapolitan_pizza = toppings.MarinaraSauce(neapolitan_pizza)
alfredo_neapolitan_pizza = toppings.AlfredoSauce(neapolitan_pizza)
cheese_neapolitan_pizza = toppings.Cheese(neapolitan_pizza)
olives_neapolitan_pizza = toppings.Olives(neapolitan_pizza)
onion_neapolitan_pizza = toppings.Onion(neapolitan_pizza)
bell_peppers_neapolitan_pizza = toppings.BellPeppers(neapolitan_pizza)
york_ham_neapolitan_pizza = toppings.YorkHam(neapolitan_pizza)
pepperoni_neapolitan_pizza = toppings.Pepperoni(neapolitan_pizza)


class TestMarinaraGetSize:
    def test_correct_type(self):
        actual = marinara_neapolitan_pizza.get_size()
        assert isinstance(actual, doughs.PizzaSize), f"Wrong type. Expected 'str', got {type(actual)}"

    def test_correct_value(self):
        actual = marinara_neapolitan_pizza.get_size()
        expected = doughs.PizzaSize.EXTRA_LARGE
        assert expected == actual, f"Wrong value. Expected {expected} but got {actual}."


class TestMarinaraGetDescription:
    def test_correct_type(self):
        actual = marinara_neapolitan_pizza.get_description()
        assert isinstance(actual, str), f"Wrong type. Expected 'str', got {type(actual)}"

    def test_correct_value(self):
        actual = marinara_neapolitan_pizza.get_description()
        expected = "Extra large Neapolitan style pizza" "\n+ Marinara sauce"
        assert expected == actual, f"Wrong value. Expected {expected} but got {actual}."


class TestMarinaraGetCost:
    def test_correct_type(self):
        actual = marinara_neapolitan_pizza.get_cost()
        assert isinstance(actual, float), f"Wrong type. Expected 'float', got {type(actual)}"

    def test_correct_value(self):
        actual = marinara_neapolitan_pizza.get_cost()
        expected = 26.0
        assert expected == actual, f"Wrong value. Expected {expected} but got {actual}."


class TestAlfredoGetSize:
    def test_correct_type(self):
        actual = alfredo_neapolitan_pizza.get_size()
        assert isinstance(actual, doughs.PizzaSize), f"Wrong type. Expected 'str', got {type(actual)}"

    def test_correct_value(self):
        actual = alfredo_neapolitan_pizza.get_size()
        expected = doughs.PizzaSize.EXTRA_LARGE
        assert expected == actual, f"Wrong value. Expected {expected} but got {actual}."


class TestalfredoGetDescription:
    def test_correct_type(self):
        actual = alfredo_neapolitan_pizza.get_description()
        assert isinstance(actual, str), f"Wrong type. Expected 'str', got {type(actual)}"

    def test_correct_value(self):
        actual = alfredo_neapolitan_pizza.get_description()
        expected = "Extra large Neapolitan style pizza" "\n+ Alfredo sauce"
        assert expected == actual, f"Wrong value. Expected {expected} but got {actual}."


class TestAlfredoGetCost:
    def test_correct_type(self):
        actual = alfredo_neapolitan_pizza.get_cost()
        assert isinstance(actual, float), f"Wrong type. Expected 'float', got {type(actual)}"

    def test_correct_value(self):
        actual = alfredo_neapolitan_pizza.get_cost()
        expected = 27.0
        assert expected == actual, f"Wrong value. Expected {expected} but got {actual}."


class TestCheeseGetSize:
    def test_correct_type(self):
        actual = cheese_neapolitan_pizza.get_size()
        assert isinstance(actual, doughs.PizzaSize), f"Wrong type. Expected 'str', got {type(actual)}"

    def test_correct_value(self):
        actual = cheese_neapolitan_pizza.get_size()
        expected = doughs.PizzaSize.EXTRA_LARGE
        assert expected == actual, f"Wrong value. Expected {expected} but got {actual}."


class TestCheeseGetDescription:
    def test_correct_type(self):
        actual = cheese_neapolitan_pizza.get_description()
        assert isinstance(actual, str), f"Wrong type. Expected 'str', got {type(actual)}"

    def test_correct_value(self):
        actual = cheese_neapolitan_pizza.get_description()
        expected = "Extra large Neapolitan style pizza" "\n+ Cheese serving"
        assert expected == actual, f"Wrong value. Expected {expected} but got {actual}."


class TestCheeseGetCost:
    def test_correct_type(self):
        actual = cheese_neapolitan_pizza.get_cost()
        assert isinstance(actual, float), f"Wrong type. Expected 'float', got {type(actual)}"

    def test_correct_value(self):
        actual = cheese_neapolitan_pizza.get_cost()
        expected = 28.0
        assert expected == actual, f"Wrong value. Expected {expected} but got {actual}."


class TestOlivesGetSize:
    def test_correct_type(self):
        actual = olives_neapolitan_pizza.get_size()
        assert isinstance(actual, doughs.PizzaSize), f"Wrong type. Expected 'str', got {type(actual)}"

    def test_correct_value(self):
        actual = olives_neapolitan_pizza.get_size()
        expected = doughs.PizzaSize.EXTRA_LARGE
        assert expected == actual, f"Wrong value. Expected {expected} but got {actual}."


class TestOlivesGetDescription:
    def test_correct_type(self):
        actual = olives_neapolitan_pizza.get_description()
        assert isinstance(actual, str), f"Wrong type. Expected 'str', got {type(actual)}"

    def test_correct_value(self):
        actual = olives_neapolitan_pizza.get_description()
        expected = "Extra large Neapolitan style pizza" "\n+ Olives serving"
        assert expected == actual, f"Wrong value. Expected {expected} but got {actual}."


class TestOlivesGetCost:
    def test_correct_type(self):
        actual = olives_neapolitan_pizza.get_cost()
        assert isinstance(actual, float), f"Wrong type. Expected 'float', got {type(actual)}"

    def test_correct_value(self):
        actual = olives_neapolitan_pizza.get_cost()
        expected = 27.0
        assert expected == actual, f"Wrong value. Expected {expected} but got {actual}."


class TestOnionGetSize:
    def test_correct_type(self):
        actual = onion_neapolitan_pizza.get_size()
        assert isinstance(actual, doughs.PizzaSize), f"Wrong type. Expected 'str', got {type(actual)}"

    def test_correct_value(self):
        actual = onion_neapolitan_pizza.get_size()
        expected = doughs.PizzaSize.EXTRA_LARGE
        assert expected == actual, f"Wrong value. Expected {expected} but got {actual}."


class TestOnionGetDescription:
    def test_correct_type(self):
        actual = onion_neapolitan_pizza.get_description()
        assert isinstance(actual, str), f"Wrong type. Expected 'str', got {type(actual)}"

    def test_correct_value(self):
        actual = onion_neapolitan_pizza.get_description()
        expected = "Extra large Neapolitan style pizza" "\n+ Onion serving"
        assert expected == actual, f"Wrong value. Expected {expected} but got {actual}."


class TestOnionGetCost:
    def test_correct_type(self):
        actual = onion_neapolitan_pizza.get_cost()
        assert isinstance(actual, float), f"Wrong type. Expected 'float', got {type(actual)}"

    def test_correct_value(self):
        actual = onion_neapolitan_pizza.get_cost()
        expected = 27.0
        assert expected == actual, f"Wrong value. Expected {expected} but got {actual}."


class TestBellPeppersGetSize:
    def test_correct_type(self):
        actual = bell_peppers_neapolitan_pizza.get_size()
        assert isinstance(actual, doughs.PizzaSize), f"Wrong type. Expected 'str', got {type(actual)}"

    def test_correct_value(self):
        actual = bell_peppers_neapolitan_pizza.get_size()
        expected = doughs.PizzaSize.EXTRA_LARGE
        assert expected == actual, f"Wrong value. Expected {expected} but got {actual}."


class TestBellPeppersGetDescription:
    def test_correct_type(self):
        actual = bell_peppers_neapolitan_pizza.get_description()
        assert isinstance(actual, str), f"Wrong type. Expected 'str', got {type(actual)}"

    def test_correct_value(self):
        actual = bell_peppers_neapolitan_pizza.get_description()
        expected = "Extra large Neapolitan style pizza" "\n+ Bell peppers serving"
        assert expected == actual, f"Wrong value. Expected {expected} but got {actual}."


class TestBellPeppersGetCost:
    def test_correct_type(self):
        actual = bell_peppers_neapolitan_pizza.get_cost()
        assert isinstance(actual, float), f"Wrong type. Expected 'float', got {type(actual)}"

    def test_correct_value(self):
        actual = bell_peppers_neapolitan_pizza.get_cost()
        expected = 26.0
        assert expected == actual, f"Wrong value. Expected {expected} but got {actual}."


class TestYorkHamGetSize:
    def test_correct_type(self):
        actual = york_ham_neapolitan_pizza.get_size()
        assert isinstance(actual, doughs.PizzaSize), f"Wrong type. Expected 'str', got {type(actual)}"

    def test_correct_value(self):
        actual = york_ham_neapolitan_pizza.get_size()
        expected = doughs.PizzaSize.EXTRA_LARGE
        assert expected == actual, f"Wrong value. Expected {expected} but got {actual}."


class TestYorkHamGetDescription:
    def test_correct_type(self):
        actual = york_ham_neapolitan_pizza.get_description()
        assert isinstance(actual, str), f"Wrong type. Expected 'str', got {type(actual)}"

    def test_correct_value(self):
        actual = york_ham_neapolitan_pizza.get_description()
        expected = "Extra large Neapolitan style pizza" "\n+ York ham serving"
        assert expected == actual, f"Wrong value. Expected {expected} but got {actual}."


class TestYorkHamGetCost:
    def test_correct_type(self):
        actual = york_ham_neapolitan_pizza.get_cost()
        assert isinstance(actual, float), f"Wrong type. Expected 'float', got {type(actual)}"

    def test_correct_value(self):
        actual = york_ham_neapolitan_pizza.get_cost()
        expected = 28.0
        assert expected == actual, f"Wrong value. Expected {expected} but got {actual}."


class TestPepperoniGetSize:
    def test_correct_type(self):
        actual = pepperoni_neapolitan_pizza.get_size()
        assert isinstance(actual, doughs.PizzaSize), f"Wrong type. Expected 'str', got {type(actual)}"

    def test_correct_value(self):
        actual = pepperoni_neapolitan_pizza.get_size()
        expected = doughs.PizzaSize.EXTRA_LARGE
        assert expected == actual, f"Wrong value. Expected {expected} but got {actual}."


class TestPepperoniGetDescription:
    def test_correct_type(self):
        actual = pepperoni_neapolitan_pizza.get_description()
        assert isinstance(actual, str), f"Wrong type. Expected 'str', got {type(actual)}"

    def test_correct_value(self):
        actual = pepperoni_neapolitan_pizza.get_description()
        expected = "Extra large Neapolitan style pizza" "\n+ Pepperoni serving"
        assert expected == actual, f"Wrong value. Expected {expected} but got {actual}."


class TestPepperoniGetCost:
    def test_correct_type(self):
        actual = pepperoni_neapolitan_pizza.get_cost()
        assert isinstance(actual, float), f"Wrong type. Expected 'float', got {type(actual)}"

    def test_correct_value(self):
        actual = pepperoni_neapolitan_pizza.get_cost()
        expected = 28.0
        assert expected == actual, f"Wrong value. Expected {expected} but got {actual}."
