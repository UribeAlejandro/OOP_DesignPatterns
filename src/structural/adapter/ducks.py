import abc


class Duck(abc.ABC):
    """Duck interface."""

    @abc.abstractmethod
    def quack(self) -> str:
        """Returns the sound made by a duck.

        Returns:
            str: Duck quacking sound
        """
        ...

    @abc.abstractmethod
    def fly(self) -> str: ...


class MallardDuck(Duck):
    """Mallard duck concrete class."""

    def quack(self) -> str:
        """Returns the sound made by a Mallard duck.

        Returns:
            str: Duck quacking sound
        """
        return "quack quackkkk!!"

    def fly(self) -> str:
        return "Flying like a Mallard Duck"
