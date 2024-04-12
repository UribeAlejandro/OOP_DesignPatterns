from src.structural.decorator import doughs


class PizzaTopping(doughs.PizzaIngredient):
    _cost: float
    _description: str
    _size: doughs.PizzaSize
    _wrapee: doughs.PizzaIngredient

    def get_size(self) -> doughs.PizzaSize:
        """Returns pizza size.

        Returns:
            doughs.PizzaSize: Pizza size
        """
        return self._wrapee.get_size()

    def get_description(self) -> str:
        """Gets the pizza's description based on the ingredients.

        Returns:
            str: Composed description of the pizza until this ingredient
        """
        return self._wrapee.get_description() + self._description

    def get_cost(self) -> float:
        """Gets the pizza's cost based on the ingredients and size.

        Returns:
            float: Composed cost of the pizza until this ingredient
        """
        return self._wrapee.get_cost() + self._cost * self.size_overcharge[self._size]


class MarinaraSauce(PizzaTopping):
    """Marinara sauce."""

    def __init__(self, base: doughs.PizzaIngredient):
        self._description = "\n+ Marinara sauce"
        self._cost = 1.0
        self._wrapee = base
        self._size = self.get_size()


class AlfredoSauce(PizzaTopping):
    """Alfredo sauce."""

    def __init__(self, base: doughs.PizzaIngredient):
        self._description = "\n+ Alfredo sauce"
        self._cost = 1.5
        self._wrapee = base
        self._size = self.get_size()


class Cheese(PizzaTopping):
    """Cheese topping."""

    def __init__(self, base: doughs.PizzaIngredient):
        self._description = "\n+ Cheese serving"
        self._cost = 2.0
        self._wrapee = base
        self._size = self.get_size()


class Olives(PizzaTopping):
    """Olives topping."""

    def __init__(self, base: doughs.PizzaIngredient):
        self._description = "\n+ Olives serving"
        self._cost = 1.5
        self._wrapee = base
        self._size = self.get_size()


class Onion(PizzaTopping):
    """Onion topping."""

    def __init__(self, base: doughs.PizzaIngredient):
        self._description = "\n+ Onion serving"
        self._cost = 1.5
        self._wrapee = base
        self._size = self.get_size()


class BellPeppers(PizzaTopping):
    """Bell peppers topping."""

    def __init__(self, base: doughs.PizzaIngredient):
        self._description = "\n+ Bell peppers serving"
        self._cost = 1.0
        self._wrapee = base
        self._size = self.get_size()


class YorkHam(PizzaTopping):
    """York ham topping."""

    def __init__(self, base: doughs.PizzaIngredient):
        self._description = "\n+ York ham serving"
        self._cost = 2.0
        self._wrapee = base
        self._size = self.get_size()


class Pepperoni(PizzaTopping):
    """Pepperoni topping."""

    def __init__(self, base: doughs.PizzaIngredient):
        self._description = "\n+ Pepperoni serving"
        self._cost = 2.0
        self._wrapee = base
        self._size = self.get_size()
