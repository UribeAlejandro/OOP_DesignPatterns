from src.structural.decorator import doughs, main, toppings


class TestPizzaOrder1:
    def test_correct_order_value(self):
        base_dough = doughs.NeapolitanPizza(doughs.PizzaSize.MEDIUM)
        pizza = main.PizzaOrder(
            dough=base_dough,
            ingredients=[
                toppings.MarinaraSauce,
                toppings.Cheese,
                toppings.Pepperoni,
                toppings.Pepperoni,
            ],
        )
        actual = str(pizza)
        expected = (
            "Medium Neapolitan style pizza\n+ Marinara sauce"
            "\n+ Cheese serving\n+ Pepperoni serving"
            "\n+ Pepperoni serving\n--------------------"
            "\nTotal cost: $22.80"
        )
        assert expected == actual, f"Wrong value. Expected {expected} but got {actual}."


class TestPizzaOrder2:
    def test_correct_order_value(self):
        base_dough = doughs.SicilianPizza(doughs.PizzaSize.LARGE)
        pizza = main.PizzaOrder(
            dough=base_dough,
            ingredients=[
                toppings.MarinaraSauce,
                toppings.MarinaraSauce,
                toppings.Cheese,
                toppings.Cheese,
                toppings.Onion,
                toppings.Pepperoni,
            ],
        )
        actual = str(pizza)
        expected = (
            "Large Sicilian style pizza\n+ Marinara sauce"
            "\n+ Marinara sauce\n+ Cheese serving"
            "\n+ Cheese serving\n+ Onion serving"
            "\n+ Pepperoni serving\n--------------------"
            "\nTotal cost: $29.25"
        )
        assert expected == actual, f"Wrong value. Expected {expected} but got {actual}."


class TestPizzaOrder3:
    def test_correct_order_value(self):
        base_dough = doughs.SicilianPizza(doughs.PizzaSize.EXTRA_LARGE)
        pizza = main.PizzaOrder(
            dough=base_dough,
            ingredients=[
                toppings.AlfredoSauce,
                toppings.Cheese,
                toppings.Onion,
                toppings.BellPeppers,
                toppings.YorkHam,
            ],
        )
        actual = str(pizza)
        expected = (
            "Extra large Sicilian style pizza\n+ Alfredo sauce"
            "\n+ Cheese serving\n+ Onion serving\n+ Bell peppers serving"
            "\n+ York ham serving\n--------------------"
            "\nTotal cost: $36.00"
        )
        assert expected == actual, f"Wrong value. Expected {expected} but got {actual}."
