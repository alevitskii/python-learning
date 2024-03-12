from abc import ABC, abstractmethod


class CaffeineBeverageWithHook:
    def prepare_recipe(self) -> None:
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments():
            self.add_condiments()

    @abstractmethod
    def brew(self) -> None:
        pass

    @abstractmethod
    def add_condiments(self) -> None:
        pass

    def boil_water(self) -> None:
        print("Boiling water")

    def pour_in_cup(self) -> None:
        print("Pouring into cup")

    def customer_wants_condiments(self) -> bool:
        return True


class CoffeeWithHook(CaffeineBeverageWithHook):
    def brew(self) -> None:
        print("Dripping Coffee through filter")

    def add_condiments(self) -> None:
        print("Adding Sugar and Milk")

    def customer_wants_condiments(self) -> bool:
        answer = self.get_user_input()
        return answer.lower().startswith("y")

    def get_user_input(self):
        return input("Would you like milk and sugar with your coffee (y/n)? ")


class TeaWithHook(CaffeineBeverageWithHook):
    def brew(self) -> None:
        print("Steeping the tea")

    def add_condiments(self) -> None:
        print("Adding Lemon")

    def customer_wants_condiments(self) -> bool:
        answer = self.get_user_input()
        return answer.lower().startswith("y")

    def get_user_input(self):
        return input("Would you like lemon with your tea (y/n)? ")


def main() -> None:
    tea_hook = TeaWithHook()
    coffee_hook = CoffeeWithHook()

    print("\nMaking tea...")
    tea_hook.prepare_recipe()

    print("\nMaking coffee...")
    coffee_hook.prepare_recipe()


if __name__ == "__main__":
    main()
