from abc import ABC, abstractmethod
from typing import override


# if we didn't have defaults for all the methods here, we could make
# a pizza protocol and had create_pizza return it so we could verify
# that each particular pizza had all the required methods defined
class Pizza:
    def __init__(self) -> None:
        self.name = None
        self.dough = None
        self.sauce = None
        self.toppings = []

    def prepare(self):
        print(f"Prepare {self.name}")
        print("Tossing dough...")
        print("Adding sauce...")
        print("Adding toppings: ")
        for topping in self.toppings:
            print(f"   {topping}")

    def bake(self):
        print("Bake for 25 minutes at 350")

    def cut(self):
        print("Cut the pizza into diagonal slices")

    def box(self):
        print("Place pizza in official PizzaStore box")


class ChicagoStylePepperoniPizza(Pizza):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Chicago Style Pepperoni Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings.append("Shredded Mozzarella Cheese")
        self.toppings.append("Black Olives")
        self.toppings.append("Spinach")
        self.toppings.append("Eggplant")
        self.toppings.append("Sliced Pepperoni")

    @override
    def cut(self):
        print("Cutting the pizza into square slices")


class ChicagoStyleClamPizza(Pizza):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Chicago Style Clam Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings.append("Shredded Mozzarella Cheese")
        self.toppings.append("Frozen Clams from Chesapeake Bay")

    @override
    def cut(self):
        print("Cutting the pizza into square slices")


class NYStylePepperoniPizza(Pizza):
    def __init__(self) -> None:
        super().__init__()
        self.name = "NY Style Pepperoni Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings.append("Grated Reggiano Cheese")
        self.toppings.append("Sliced Pepperoni")
        self.toppings.append("Garlic")
        self.toppings.append("Onion")
        self.toppings.append("Mushrooms")
        self.toppings.append("Red Pepper")


class NYStyleClamPizza(Pizza):
    def __init__(self) -> None:
        super().__init__()
        self.name = "NY Style Clam Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings.append("Grated Reggiano Cheese")
        self.toppings.append("Fresh Clams from Long Island Sound")


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
        if item == "clam":
            return ChicagoStyleClamPizza()
        elif item == "pepperoni":
            return ChicagoStylePepperoniPizza()
        raise ValueError(f"Invalid pizza type {item}")


class NYPizzaStore(PizzaStore):
    def create_pizza(self, item: str) -> Pizza:
        if item == "clam":
            return NYStyleClamPizza()
        elif item == "pepperoni":
            return NYStylePepperoniPizza()
        raise ValueError(f"Invalid pizza type {item}")


def main() -> None:
    ny_store = NYPizzaStore()
    chicago_store = ChicagoPizzaStore()

    pizza = ny_store.order_pizza("clam")
    print(f"Ethan ordered a {pizza.name}")

    pizza = chicago_store.order_pizza("clam")
    print(f"Joel ordered a {pizza.name}")

    pizza = ny_store.order_pizza("pepperoni")
    print(f"Ethan ordered a {pizza.name}")

    pizza = chicago_store.order_pizza("pepperoni")
    print(f"Joel ordered a {pizza.name}")


if __name__ == "__main__":
    main()
