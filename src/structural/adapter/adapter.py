from src.structural.adapter.drones import Drone
from src.structural.adapter.ducks import Duck


class DroneAdapter(Duck):
    """Drone Adapter class, implements Duck Interface."""

    def __init__(self, drone: Drone) -> None:
        """_summary_

        Args:
            drone (Drone): Drone subclass that will be adapted to follow Duck's
            behaviour.
        """
        super().__init__()
        self.drone: Drone = drone

    def quack(self) -> str:
        """Quack method adapted to return drone's beeping sound.

        Returns:
            str: Drone's beeping sound.
        """
        return self.drone.beep()

    def fly(self) -> str:
        """Fly method adapted to return drone's fly action.

        Returns:
            str: Drone's taking off action.
        """
        return self.drone.spin_rotors() + "\n" + self.drone.take_off()
