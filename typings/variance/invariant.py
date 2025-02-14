class Beverage:
    """Any beverage."""


class Juice(Beverage):
    """Any fruit juice."""


class OrangeJuice(Juice):
    """Delicious juice from Brazilian oranges."""


class BeverageDispenser[T]:
    """A dispenser parameterized on the beverage type."""

    def __init__(self, beverage: T) -> None:
        self.beverage = beverage

    def dispense(self) -> T:
        return self.beverage


def install(dispenser: BeverageDispenser[Juice]) -> None:
    """Install a fruit juice dispenser."""


juice_dispenser = BeverageDispenser(Juice())
install(juice_dispenser)

beverage_dispenser = BeverageDispenser(Beverage())
# Argument 1 to "install" has incompatible type "BeverageDispenser[Beverage]" expected "BeverageDispenser[Juice]"
install(beverage_dispenser)  # type: ignore

orange_juice_dispenser = BeverageDispenser(OrangeJuice())
# Argument 1 to "install" has incompatible type "BeverageDispenser[OrangeJuice]" expected "BeverageDispenser[Juice]"
install(orange_juice_dispenser)  # type: ignore
