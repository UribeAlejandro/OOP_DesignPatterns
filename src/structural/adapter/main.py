from src.structural.adapter import adapter, drones, ducks


class DuckSimulator:
    """Simulates a duck general behavior."""

    @staticmethod
    def simulate_duck(duck: ducks.Duck) -> str:
        """Simulates sound and fly of a duck.

        Args:
            duck (ducks.Duck): Duck object to be simulated
        """
        return f"{duck.quack()}\n{duck.fly()}"

    def main(self, *args: str) -> None:
        duck: ducks.Duck = ducks.MallardDuck()
        print(self.simulate_duck(duck))

        drone: drones.Drone = drones.SuperDrone()
        adapted_drone: adapter.DroneAdapter = adapter.DroneAdapter(drone)
        print(self.simulate_duck(adapted_drone))


if __name__ == "__main__":
    simulator = DuckSimulator()
    simulator.main()
