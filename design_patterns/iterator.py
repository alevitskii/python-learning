from collections.abc import Iterator
from typing import Protocol


class MenuItem:
    def __init__(self, name: str, description: str, vegeterian: bool, price: float) -> None:
        self._name = name
        self._desciption = description
        self._vegeterian = vegeterian
        self._price = price

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._desciption

    @property
    def vegeterian(self) -> bool:
        return self._vegeterian

    @property
    def price(self) -> float:
        return self._price


class MenuProtocol(Protocol):
    def __iter__(self) -> Iterator: ...
    def __getitem__(self, index: int) -> MenuItem: ...


class DinerMenuIterator(Iterator):
    def __init__(self, menu_items: MenuProtocol) -> None:
        self._menu_items = menu_items
        self._position: int = 0

    def __next__(self) -> MenuItem:
        try:
            value = self._menu_items[self._position]
            self._position += 1
        except IndexError:
            raise StopIteration()
        return value


class PancakeHouseMenu:
    def __init__(self) -> None:
        self._menu_items = []
        self.add_item(
            name="K&B's Pancake Breakfast",
            description="Pancakes with scrambled eggs, and toast",
            vegeterian=True,
            price=2.99,
        )
        self.add_item(
            name="Regular Pancake Breakfast",
            description="Pancakes with fried eggs, sausage",
            vegeterian=False,
            price=2.99,
        )
        self.add_item(
            name="Blueberry Pancakes",
            description="Pancakes made with fresh blueberries, and blueberry syrup",
            vegeterian=True,
            price=3.49,
        )
        self.add_item(
            name="Waffles",
            description="Waffles, with your choice of blueberries or strawberries",
            vegeterian=True,
            price=3.59,
        )

    def add_item(self, name: str, description: str, vegeterian: bool, price: float) -> None:
        self._menu_items.append(MenuItem(name=name, description=description, vegeterian=vegeterian, price=price))

    def __getitem__(self, index: int) -> MenuItem:
        return self._menu_items[index]

    def __iter__(self) -> DinerMenuIterator:
        return DinerMenuIterator(self)


class DinerMenu:
    MAX_ITEMS = 6

    def __init__(self) -> None:
        super().__init__()
        self._menu_items = []
        self.add_item(
            name="Vegetarian BLT",
            description="(Fakin') Bacon with lettuce & tomato on whole wheat",
            vegeterian=True,
            price=2.99,
        )
        self.add_item(
            name="BLT",
            description="Bacon with lettuce & tomato on whole wheat",
            vegeterian=False,
            price=2.99,
        )
        self.add_item(
            name="Soup of the day",
            description="Soup of the day, with a side of potato salad",
            vegeterian=False,
            price=3.29,
        )
        self.add_item(
            name="Steamed Veggies and Brown Rice",
            description="Steamed vegetables over brown rice",
            vegeterian=True,
            price=3.99,
        )
        self.add_item(
            name="Pasta",
            description="Spaghetti with Marinara Sauce, and a slice of sourdough bread",
            vegeterian=True,
            price=3.89,
        )

    def add_item(self, name: str, description: str, vegeterian: bool, price: float) -> None:
        if len(self._menu_items) >= self.MAX_ITEMS:
            print("Sorry, menu is full!  Can't add item to menu")
        else:
            self._menu_items.append(MenuItem(name=name, description=description, vegeterian=vegeterian, price=price))

    def __getitem__(self, index: int) -> MenuItem:
        return self._menu_items[index]

    def __iter__(self) -> DinerMenuIterator:
        return DinerMenuIterator(self)


class Waitress:
    def __init__(self, pancake_house_menu: PancakeHouseMenu, diner_menu: DinerMenu) -> None:
        self.pancake_house_menu = pancake_house_menu
        self.diner_menu = diner_menu

    def print_menu(self):
        pancake_iterator = iter(self.pancake_house_menu)
        diner_iterator = iter(self.diner_menu)
        print("MENU\n----\nBREAKFAST")
        self.print_concrete_menu(pancake_iterator)
        print("\nLUNCH")
        self.print_concrete_menu(diner_iterator)

    def print_concrete_menu(self, iterator: Iterator[MenuItem]):
        for item in iterator:
            print(f"{item.name}, {item.price} -- {item.description}")


def main() -> None:
    pancake_house_menu = PancakeHouseMenu()
    diner_menu = DinerMenu()
    waitress = Waitress(pancake_house_menu, diner_menu)
    waitress.print_menu()


if __name__ == "__main__":
    main()
