# Implementation looks contrived
# Iteration is an intrinsic feature of Python
# Probably solution for such a task can be built more "pythonically"
from abc import ABC, abstractmethod
from collections.abc import Iterator
from typing import NoReturn, Self


class MenuComponent(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        pass

    @property
    def price(self) -> str:
        raise NotImplementedError()

    @property
    def vegetarian(self) -> str:
        raise NotImplementedError()

    def add(self, menu_component: Self) -> None:
        raise NotImplementedError()

    def remove(self, menu_component: Self) -> None:
        raise NotImplementedError()

    def get_child(self, i: int) -> Self:
        raise NotImplementedError()

    @abstractmethod
    def __iter__(self) -> Iterator[Self]:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class NullIterator(Iterator):
    def __next__(self) -> NoReturn:
        raise StopIteration()


class CompositeIterator(Iterator):
    def __init__(self, iterator: Iterator[MenuComponent]) -> None:
        self.stack: list[Iterator[MenuComponent]] = [iterator]

    def __next__(self) -> MenuComponent:
        if self.stack:
            iterator = self.stack[-1]
            try:
                mc = next(iterator)
            except StopIteration:
                self.stack.pop()
                self.__next__()
            else:
                return mc
        raise StopIteration()


class MenuItem(MenuComponent):
    def __init__(self, name: str, description: str, vegetarian: bool, price: float) -> None:
        self._name = name
        self._description = description
        self._vegetarian = vegetarian
        self._price = price

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description

    @property
    def vegetarian(self) -> bool:
        return self._vegetarian

    @property
    def price(self) -> float:
        return self._price

    def __str__(self) -> str:
        s = ""
        s += f" {self._name}"
        if self._vegetarian:
            s += "(v)"
        s += f", {self._price}"
        s += f"     -- {self._description}\n"
        return s

    def __iter__(self) -> Iterator:
        return NullIterator()


class Menu(MenuComponent):
    def __init__(self, name: str, description: str) -> None:
        self._name = name
        self._description = description
        self._menu_components: list[MenuComponent] = []
        self._iterator = None

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description

    def add(self, menu_component: MenuComponent) -> None:
        self._menu_components.append(menu_component)

    def remove(self, menu_component: MenuComponent) -> None:
        self._menu_components.remove(menu_component)

    def get_child(self, i: int) -> MenuComponent:
        return self._menu_components[i]

    def __str__(self) -> str:
        s = ""
        s += f"\n{self._name}"
        s += f", {self._description}\n"
        s += "---------------------\n"
        for mc in self._menu_components:
            s += str(mc)
        return s

    def __iter__(self) -> Iterator[MenuComponent]:
        if self._iterator is None:
            self._iterator = CompositeIterator(iter(self._menu_components))
        return self._iterator


class Waitress:
    def __init__(self, all_menus: MenuComponent) -> None:
        self.all_menus = all_menus

    def print_menu(self):
        print(self.all_menus)


def main() -> None:
    pancake_house_menu = Menu("PANCAKE HOUSE MENU", "Breakfast")
    diner_menu = Menu("DINER MENU", "Lunch")
    cafe_menu = Menu("CAFE MENU", "Dinner")
    dessert_menu = Menu("DESSERT MENU", "Dessert of course!")

    all_menus = Menu("ALL MENUS", "All menus combined")

    all_menus.add(pancake_house_menu)
    all_menus.add(diner_menu)
    all_menus.add(cafe_menu)

    pancake_house_menu.add(MenuItem("K&B's Pancake Breakfast", "Pancakes with scrambled eggs and toast", True, 2.99))
    pancake_house_menu.add(MenuItem("Regular Pancake Breakfast", "Pancakes with fried eggs, sausage", False, 2.99))
    pancake_house_menu.add(
        MenuItem("Blueberry Pancakes", "Pancakes made with fresh blueberries and blueberry syrup", True, 3.49)
    )
    pancake_house_menu.add(MenuItem("Waffles", "Waffles with your choice of blueberries or strawberries", True, 3.59))

    diner_menu.add(MenuItem("Vegetarian BLT", "(Fakin') Bacon with lettuce & tomato on whole wheat", True, 2.99))
    diner_menu.add(MenuItem("BLT", "Bacon with lettuce & tomato on whole wheat", False, 2.99))
    diner_menu.add(
        MenuItem("Soup of the day", "A bowl of the soup of the day, with a side of potato salad", False, 3.29)
    )
    diner_menu.add(MenuItem("Hot Dog", "A hot dog, with saurkraut, relish, onions, topped with cheese", False, 3.05))
    diner_menu.add(
        MenuItem("Steamed Veggies and Brown Rice", "A medly of steamed vegetables over brown rice", True, 3.99)
    )

    diner_menu.add(MenuItem("Pasta", "Spaghetti with marinara sauce, and a slice of sourdough bread", True, 3.89))

    diner_menu.add(dessert_menu)

    dessert_menu.add(MenuItem("Apple Pie", "Apple pie with a flakey crust, topped with vanilla icecream", True, 1.59))
    dessert_menu.add(MenuItem("Cheesecake", "Creamy York cheesecake, with a chocolate graham crust", True, 1.99))
    dessert_menu.add(MenuItem("Sorbet", "A scoop of raspberry and a scoop of lime", True, 1.89))

    cafe_menu.add(
        MenuItem(
            "Veggie Burger and Air Fries", "Veggie burger on a whole wheat bun, lettuce, tomato, and fries", True, 3.99
        )
    )
    cafe_menu.add(MenuItem("Soup of the day", "A cup of the soup of the day, with a side salad", False, 3.69))
    cafe_menu.add(MenuItem("Burrito", "A large burrito, with whole pinto beans, salsa, guacamole", True, 4.29))

    waitress = Waitress(all_menus)

    waitress.print_menu()


if __name__ == "__main__":
    main()
