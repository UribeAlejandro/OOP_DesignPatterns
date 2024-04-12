import abc


class Drone(abc.ABC):
    """Drone interface."""

    @abc.abstractmethod
    def beep(self) -> str:
        """Returns drone's beeping sound.

        Returns:
            str: Drone's beeping sound
        """
        ...

    @abc.abstractmethod
    def spin_rotors(self) -> str:
        """Returns drone's rotors spinning action.

        Returns:
            str: Drone's rotors spinning action
        """
        ...

    @abc.abstractmethod
    def take_off(self) -> str:
        """Returns drone's taking off action.

        Returns:
            str: Drone's taking off action
        """
        ...


class SuperDrone(Drone):
    def beep(self) -> str:
        """Returns super drone's beeping sound.

        Returns:
            str: Super drone's beeping sound
        """
        return "Beep beep beep"

    def spin_rotors(self) -> str:
        """Returns super drone's rotors spinning action.

        Returns:
            str: Super drone's rotors spinning action
        """
        return "Rotors are spinning"

    def take_off(self) -> str:
        """Returns super drone's taking off action.

        Returns:
            str: Super drone's taking off action
        """
        return "Taking off"
