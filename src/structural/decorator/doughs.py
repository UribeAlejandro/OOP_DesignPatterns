import abc
import enum
from typing import Dict


class PizzaSize(str, enum.Enum):
    """Enumeration for pizza sizes."""

    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"
    EXTRA_LARGE = "Extra large"


class PizzaIngredient(abc.ABC):
    """Pizza ingredients interface."""

    size_overcharge: Dict[PizzaSize, float] = {
        PizzaSize.SMALL: 1,
        PizzaSize.MEDIUM: 1.2,
        PizzaSize.LARGE: 1.5,
        PizzaSize.EXTRA_LARGE: 2,
    }

    @abc.abstractmethod
    def get_size(self) -> PizzaSize:
        """Returns the pizza size.

        Returns:
            PizzaSize: Pizza size
        """
        ...

    @abc.abstractmethod
    def get_description(self) -> str:
        """Returns the decription.

        Returns:
            str: Description
        """
        ...

    @abc.abstractmethod
    def get_cost(self) -> float:
        """Returns the cost.

        Returns:
            float: Cost
        """
        ...


class PizzaDough(PizzaIngredient):
    """Pizza dough class."""

    _cost: float
    _description: str
    _size: PizzaSize

    def get_size(self) -> PizzaSize:
        """Returns the pizza size.

        Returns:
            PizzaSize: Pizza size
        """
        return self._size

    def get_description(self) -> str:
        """Gets the pizza's description based on the dough.

        Returns:
            str: Composed description of the pizza dough
        """
        return self._size + " " + self._description

    def get_cost(self) -> float:
        """Gets the pizza's cost based on the dough and size.

        Returns:
            float: Composed cost of the pizza dough
        """
        return self._cost * self.size_overcharge[self._size]


class SicilianPizza(PizzaDough):
    """Sicilian dough."""

    def __init__(self, size: PizzaSize):
        self._description = "Sicilian style pizza"
        self._cost = 10.0
        self._size = size


class NeapolitanPizza(PizzaDough):
    """Neapolitan dough."""

    def __init__(self, size: PizzaSize):
        self._description = "Neapolitan style pizza"
        self._cost = 12.0
        self._size = size
