from typing import List

from src.structural.decorator import doughs, toppings


class PizzaOrder:
    """Class to represent a pizza order."""

    def __init__(
        self,
        dough: doughs.PizzaDough,
        ingredients: List[doughs.PizzaIngredient],
    ):
        self._dough = dough
        self._ingredients = ingredients
        self._pizza = self.compose_pizza()

    def compose_pizza(self) -> doughs.PizzaIngredient:
        """Composes the ingredients to create a pizza.

        Returns:
            doughs.PizzaIngredient: Pizza after composing the ingredients
        """
        pizza: doughs.PizzaIngredient = self._dough

        for ingredient in self._ingredients:
            pizza = ingredient(pizza)

        return pizza

    def get_total_cost(self) -> float:
        """Gets the total cost of the pizza.

        Returns:
            float: Total cost of the pizza
        """
        return self._pizza.get_cost()

    def get_full_description(self) -> str:
        return self._pizza.get_description()

    def __str__(self) -> str:
        """Returns the pizza order as string.

        Returns:
            str: Pizza order for printing
        """
        return self.get_full_description() + "\n--------------------" + f"\nTotal cost: ${self.get_total_cost():.2f}"


if __name__ == "__main__":
    pizza_dough = doughs.NeapolitanPizza(doughs.PizzaSize.SMALL)
    ingredients = [
        toppings.MarinaraSauce,
        toppings.Cheese,
        toppings.Pepperoni,
        toppings.Pepperoni,
    ]

    pizza_order = PizzaOrder(dough=pizza_dough, ingredients=ingredients)

    print(pizza_order)
