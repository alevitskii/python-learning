import random
from typing import Protocol


class DuckProtocol(Protocol):
    def quack(self) -> None: ...
    def fly(self) -> None: ...


class TurkeyProtocol(Protocol):
    def gobble(self) -> None: ...
    def fly(self) -> None: ...


class DroneProtocol(Protocol):
    def beep(self) -> None: ...
    def spin_rotors(self) -> None: ...
    def take_off(self) -> None: ...


class DuckAdapter:
    def __init__(self, duck: DuckProtocol) -> None:
        self.duck = duck

    def gobble(self) -> None:
        self.duck.quack()

    def fly(self) -> None:
        if random.randint(0, 5) == 0:
            self.duck.fly()


class TurkeyAdapter:
    def __init__(self, turkey: TurkeyProtocol) -> None:
        self.turkey = turkey

    def quack(self) -> None:
        self.turkey.gobble()

    def fly(self) -> None:
        for _ in range(5):
            self.turkey.fly()


class DroneAdapter:
    def __init__(self, drone: DroneProtocol) -> None:
        self.drone = drone

    def quack(self) -> None:
        self.drone.beep()

    def fly(self) -> None:
        self.drone.spin_rotors()
        self.drone.take_off()


class MallardDuck:
    def quack(self) -> None:
        print("Quack")

    def fly(self) -> None:
        print("I'm flying")


class WildTurkey:
    def gobble(self) -> None:
        print("Gobble gobble")

    def fly(self) -> None:
        print("I'm flying a short distance")


class SuperDrone:
    def beep(self) -> None:
        print("Beep beep beep")

    def spin_rotors(self) -> None:
        print("Rotors are spinning")

    def take_off(self) -> None:
        print("Taking off")


def test_duck(duck: DuckProtocol) -> None:
    duck.quack()
    duck.fly()


def main() -> None:
    duck = MallardDuck()

    turkey = WildTurkey()
    turkey_adapter: DuckProtocol = TurkeyAdapter(turkey)

    print("The Turkey says...")
    turkey.gobble()
    turkey.fly()

    print("\nThe Duck says...")
    test_duck(duck)

    print("\nThe TurkeyAdapter says...")
    test_duck(turkey_adapter)

    duck_adapter: TurkeyProtocol = DuckAdapter(duck)
    for _ in range(10):
        print("The DuckAdapter says...")
        duck_adapter.gobble()
        duck_adapter.fly()

    drone = SuperDrone()
    drone_adapter: DuckProtocol = DroneAdapter(drone)
    test_duck(drone_adapter)


if __name__ == "__main__":
    main()
