from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import override


class Size(Enum):
    TALL = auto()
    GRANDE = auto()
    VENTI = auto()


class Beverage(ABC):
    def __init__(self) -> None:
        self._size = Size.TALL
        self._description = "Unknown Beverage"

    @property
    def size(self) -> Size:
        return self._size

    @size.setter
    def size(self, size) -> None:
        self._size = size

    def get_description(self) -> str:
        return self._description

    @abstractmethod
    def cost(self) -> float:
        pass


class Espresso(Beverage):
    def __init__(self) -> None:
        super().__init__()
        self._description = "Espresso"

    def cost(self) -> float:
        return 1.99


class HouseBlend(Beverage):
    def __init__(self) -> None:
        super().__init__()
        self._description = "House Blend Coffee"

    def cost(self) -> float:
        return 0.89


class DarkRoast(Beverage):
    def __init__(self) -> None:
        super().__init__()
        self._description = "Dark Roast Coffee"

    def cost(self) -> float:
        return 0.99


class CondimentDecorator(Beverage):
    def __init__(self, beverage: Beverage) -> None:
        super().__init__()
        self._beverage = beverage


class Milk(CondimentDecorator):
    # making get_description an abstract method in CondimentDecorator might be too much
    @override
    def get_description(self) -> str:
        return f"{self._beverage.get_description()}, Milk"

    def cost(self) -> float:
        return self._beverage.cost() + 0.10


class Whip(CondimentDecorator):
    @override
    def get_description(self) -> str:
        return f"{self._beverage.get_description()}, Whip"

    def cost(self) -> float:
        return self._beverage.cost() + 0.10


class Mocha(CondimentDecorator):
    @override
    def get_description(self) -> str:
        return f"{self._beverage.get_description()}, Mocha"

    def cost(self) -> float:
        return self._beverage.cost() + 0.10


class Soy(CondimentDecorator):
    @override
    def get_description(self) -> str:
        return f"{self._beverage.get_description()}, Soy"

    def cost(self) -> float:
        cost = self._beverage.cost()
        if self._beverage.size == Size.TALL:
            cost += 0.10
        elif self._beverage.size == Size.GRANDE:
            cost += 0.15
        elif self._beverage.size == Size.VENTI:
            cost += 0.20
        return cost


def main() -> None:
    beverage = Espresso()
    print(f"{beverage.get_description()} ${beverage.cost():.2f}")

    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print(f"{beverage2.get_description()} ${beverage2.cost():.2f}")

    beverage3 = HouseBlend()
    beverage3.size = Size.VENTI
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(f"{beverage3.get_description()} ${beverage3.cost():.2f}")


if __name__ == "__main__":
    main()
