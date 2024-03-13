from abc import ABC, abstractmethod
from collections.abc import Sequence
from typing import Protocol


class _Dough(Protocol):
    def __str__(self) -> str: ...


class ThickCrustDough:
    def __str__(self) -> str:
        return "ThickCrust style extra thick crust dough"


class ThinCrustDough:
    def __str__(self) -> str:
        return "Thin Crust Dough"


class _Cheese(Protocol):
    def __str__(self) -> str: ...


class MozzarellaCheese:
    def __str__(self) -> str:
        return "Shredded Mozzarella"


class ReggianoCheese:
    def __str__(self) -> str:
        return "Reggiano Cheese"


class _Veggies(Protocol):
    def __str__(self) -> str: ...


class Spinach:
    def __str__(self) -> str:
        return "Spinach"


class Onion:
    def __str__(self) -> str:
        return "Onion"


class _PizzaIngredientFactory(Protocol):
    def create_dough(self) -> _Dough: ...
    def create_cheese(self) -> _Cheese: ...
    def create_veggies(self) -> Sequence[_Veggies]: ...


class ChicagoPizzaIngredientFactory:
    def create_dough(self):
        return ThickCrustDough()

    def create_cheese(self):
        return MozzarellaCheese()

    def create_veggies(self):
        return [Spinach()]


class NYPizzaIngredientFactory:
    def create_dough(self):
        return ThinCrustDough()

    def create_cheese(self):
        return ReggianoCheese()

    def create_veggies(self):
        return [Onion()]


class Pizza(ABC):
    def __init__(self) -> None:
        self._name: str = ""
        self.dough = None
        self.sauce = None
        self.toppings = []

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @abstractmethod
    def prepare(self):
        pass

    def bake(self):
        print("Bake for 25 minutes at 350")

    def cut(self):
        print("Cut the pizza into diagonal slices")

    def box(self):
        print("Place pizza in official PizzaStore box")


class CheesePizza(Pizza):
    def __init__(self, ingregient_factory: _PizzaIngredientFactory) -> None:
        super().__init__()
        self.ingredient_facrory = ingregient_factory

    def prepare(self):
        print(f"Preparing {self.name}")
        _ = self.ingredient_facrory.create_dough()
        _ = self.ingredient_facrory.create_cheese()


class VeggiePizza(Pizza):
    def __init__(self, ingregient_factory: _PizzaIngredientFactory) -> None:
        super().__init__()
        self.ingredient_facrory = ingregient_factory

    def prepare(self):
        print(f"Preparing {self.name}")
        _ = self.ingredient_facrory.create_dough()
        _ = self.ingredient_facrory.create_cheese()
        _ = self.ingredient_facrory.create_veggies()


class PizzaStore(ABC):
    @abstractmethod
    def create_pizza(self, item: str) -> Pizza:
        pass

    def order_pizza(self, type: str) -> Pizza:
        pizza = self.create_pizza(type)
        print(f"--- Making a {pizza.name} ---")
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, item: str) -> Pizza:
        ingredient_factory = ChicagoPizzaIngredientFactory()
        if item == "cheese":
            pizza = CheesePizza(ingredient_factory)
            pizza.name = "Chicago Style Cheese Pizza"
        elif item == "veggie":
            pizza = VeggiePizza(ingredient_factory)
            pizza.name = "Chicago Style Veggie Pizza"
        else:
            raise ValueError(f"Invalid pizza type {item}")
        return pizza


class NYPizzaStore(PizzaStore):
    def create_pizza(self, item: str) -> Pizza:
        ingredient_factory = NYPizzaIngredientFactory()
        if item == "cheese":
            pizza = CheesePizza(ingredient_factory)
            pizza.name = "Chicago Style Cheese Pizza"
        elif item == "veggie":
            pizza = VeggiePizza(ingredient_factory)
            pizza.name = "Chicago Style Veggie Pizza"
        else:
            raise ValueError(f"Invalid pizza type {item}")
        return pizza


def main() -> None:
    ny_store = NYPizzaStore()
    chicago_store = ChicagoPizzaStore()

    pizza = ny_store.order_pizza("cheese")
    print(f"Ethan ordered a {pizza.name}")

    pizza = chicago_store.order_pizza("cheese")
    print(f"Joel ordered a {pizza.name}")

    pizza = ny_store.order_pizza("veggie")
    print(f"Ethan ordered a {pizza.name}")

    pizza = chicago_store.order_pizza("veggie")
    print(f"Joel ordered a {pizza.name}")


if __name__ == "__main__":
    main()
