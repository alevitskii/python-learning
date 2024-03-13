from abc import ABC, abstractmethod
from typing import Protocol


class _FlyBehavior(Protocol):
    def fly(self) -> None: ...


class FlyWithWings:
    def fly(self) -> None:
        print("I'm flying!")


class FlyNoWay:
    def fly(self) -> None:
        print("I can't fly")


class FlyRocketPowered:
    def fly(self) -> None:
        print("I'm flying with a rocket")


class _QuackBehavior(Protocol):
    def quack(self) -> None: ...


class Quack:
    def quack(self) -> None:
        print("Quack")


class MuteQuack:
    def quack(self) -> None:
        print("<< Silence >>")


class Squeak:
    def quack(self) -> None:
        print("Squeak")


class FakeQuack:
    def quack(self) -> None:
        print("Qwak")


# not sure about ABC here
class Duck(ABC):
    def __init__(self, fly_behavior: _FlyBehavior, quack_behavior: _QuackBehavior) -> None:
        self._fly_behavior = fly_behavior
        self._quack_behavior = quack_behavior

    @property
    def fly_behavior(self) -> _FlyBehavior:
        return self._fly_behavior

    @fly_behavior.setter
    def fly_behavior(self, fly_behavior: _FlyBehavior) -> None:
        self._fly_behavior = fly_behavior

    @property
    def quack_behavior(self) -> _QuackBehavior:
        return self._quack_behavior

    @quack_behavior.setter
    def quack_behavior(self, quack_behavior: _QuackBehavior) -> None:
        self._quack_behavior = quack_behavior

    @abstractmethod
    def display(self) -> None:
        pass

    def perform_fly(self) -> None:
        self._fly_behavior.fly()

    def perform_quack(self) -> None:
        self._quack_behavior.quack()

    def swim(self) -> None:
        print("All ducks float, even decoys!")


class RedHeadDuck(Duck):
    def __init__(self) -> None:
        super().__init__(FlyWithWings(), Quack())

    def display(self) -> None:
        print("I'm a real Red Headed duck")


class RubberDuck(Duck):
    def __init__(self) -> None:
        super().__init__(FlyNoWay(), Squeak())

    def display(self) -> None:
        print("I'm a rubber duckie")


class DecoyDuck(Duck):
    def __init__(self) -> None:
        super().__init__(FlyNoWay(), MuteQuack())

    def display(self) -> None:
        print("I'm a duck Decoy")


class MallardDuck(Duck):
    def __init__(self) -> None:
        super().__init__(FlyWithWings(), Quack())

    def display(self) -> None:
        print("I'm a real Mallard duck")


class ModelDuck(Duck):
    def __init__(self) -> None:
        super().__init__(FlyNoWay(), Quack())

    def display(self) -> None:
        print("I'm a model duck")


def main() -> None:
    mallard = MallardDuck()
    mallard.perform_quack()
    mallard.perform_fly()

    model = ModelDuck()
    model.perform_fly()
    model.fly_behavior = FlyRocketPowered()
    model.perform_fly()


if __name__ == "__main__":
    main()
