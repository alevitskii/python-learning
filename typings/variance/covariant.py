from typing import Generic, TypeVar


class Beverage:
    """Any beverage."""


class Juice(Beverage):
    """Any fruit juice."""


class OrangeJuice(Juice):
    """Delicious juice from Brazilian oranges."""


T_co = TypeVar("T_co", covariant=True)


class BeverageDispenser(Generic[T_co]):
    """A dispenser parameterized on the beverage type."""

    def __init__(self, beverage: T_co) -> None:
        self.beverage = beverage

    def dispense(self) -> T_co:
        return self.beverage


def install(dispenser: BeverageDispenser[Juice]) -> None:
    """Install a fruit juice dispenser."""


juice_dispenser = BeverageDispenser(Juice())
install(juice_dispenser)

orange_juice_dispenser = BeverageDispenser(OrangeJuice())
install(orange_juice_dispenser)

beverage_dispenser = BeverageDispenser(Beverage())
# Argument 1 to "install" has incompatible type "BeverageDispenser[Beverage]" expected "BeverageDispenser[Juice]"
install(beverage_dispenser)  # type: ignore
