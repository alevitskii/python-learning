from __future__ import annotations

import random
from typing import Protocol


class _State(Protocol):
    def insert_quarter(self) -> None: ...
    def eject_quarter(self) -> None: ...
    def turn_crank(self) -> None: ...
    def dispense(self) -> None: ...
    def refill(self) -> None: ...


class GumballMachine:
    def __init__(self, number_gumballs: int) -> None:
        self._sold_out_state: _State = SoldOutState(self)
        self._no_quarter_state: _State = NoQuarterState(self)
        self._has_quarter_state: _State = HasQuarterState(self)
        self._sold_state: _State = SoldState(self)
        self._winner_state: _State = WinnerState(self)

        self._count = number_gumballs
        self._state = self._no_quarter_state if number_gumballs > 0 else self._sold_out_state

    def insert_quarter(self):
        self._state.insert_quarter()

    def eject_quarter(self):
        self._state.eject_quarter()

    def turn_crank(self):
        self._state.turn_crank()
        self._state.dispense()

    @property
    def state(self) -> _State:
        return self._state

    @state.setter
    def state(self, state: _State) -> None:
        self._state = state

    @property
    def count(self) -> int:
        return self._count

    def release_ball(self):
        print("A gumball comes rolling out the slot...")
        if self._count > 0:
            self._count -= 1

    def refill(self, count):
        self._count += count
        print(f"The gumball machine was just refilled; its new count is: {self._count}")
        self._state.refill()

    @property
    def sold_out_state(self) -> _State:
        return self._sold_out_state

    @property
    def no_quarter_state(self) -> _State:
        return self._no_quarter_state

    @property
    def has_quarter_state(self) -> _State:
        return self._has_quarter_state

    @property
    def sold_state(self) -> _State:
        return self._sold_state

    @property
    def winner_state(self) -> _State:
        return self._winner_state

    def __str__(self) -> str:
        ret = ""
        ret += "\nMighty Gumball, Inc."
        ret += "\nPython-enabled Standing Gumball Model #2004"
        ret += f"\nInventory: {self.count} gumball"
        if self.count != 1:
            ret += "s"
        ret += "\n"
        ret += f"\nMachine is {self.state}\n"
        return ret


class HasQuarterState:
    def __init__(self, gumball_machine: GumballMachine) -> None:
        self.gumball_machine = gumball_machine

    def insert_quarter(self) -> None:
        print("You can't insert another quarter")

    def eject_quarter(self) -> None:
        print("Quarter returned")
        self.gumball_machine.state = self.gumball_machine.no_quarter_state

    def turn_crank(self) -> None:
        print("You turned...")
        winner = random.randint(0, 9)
        if winner == 0 and self.gumball_machine.count > 1:
            self.gumball_machine.state = self.gumball_machine.winner_state
        else:
            self.gumball_machine.state = self.gumball_machine.sold_state

    def dispense(self) -> None:
        print("No gumball dispensed")

    def refill(self) -> None:
        pass

    def __str__(self) -> str:
        return "waiting for turn of crank"


class NoQuarterState:
    def __init__(self, gumball_machine: GumballMachine) -> None:
        self.gumball_machine = gumball_machine

    def insert_quarter(self) -> None:
        print("You inserted a quarter")
        self.gumball_machine.state = self.gumball_machine.has_quarter_state

    def eject_quarter(self) -> None:
        print("You haven't inserted a quarter")

    def turn_crank(self) -> None:
        print("You turned, but there's no quarter")

    def dispense(self) -> None:
        print("You need to pay first")

    def refill(self) -> None:
        pass

    def __str__(self) -> str:
        return "waiting for quarter"


class SoldOutState:
    def __init__(self, gumball_machine: GumballMachine) -> None:
        self.gumball_machine = gumball_machine

    def insert_quarter(self) -> None:
        print("You can't insert a quarter, the machine is sold out")

    def eject_quarter(self) -> None:
        print("You can't eject, you haven't inserted a quarter yet")

    def turn_crank(self) -> None:
        print("You turned, but there are no gumballs")

    def dispense(self) -> None:
        print("No gumball dispensed")

    def refill(self) -> None:
        self.gumball_machine.state = self.gumball_machine.no_quarter_state

    def __str__(self) -> str:
        return "sold out"


class SoldState:
    def __init__(self, gumball_machine: GumballMachine) -> None:
        self.gumball_machine = gumball_machine

    def insert_quarter(self) -> None:
        print("Please wait, we're already giving you a gumball")

    def eject_quarter(self) -> None:
        print("Sorry, you already turned the crank")

    def turn_crank(self) -> None:
        print("Turning twice doesn't get you another gumball!")

    def dispense(self) -> None:
        self.gumball_machine.release_ball()
        if self.gumball_machine.count > 0:
            self.gumball_machine.state = self.gumball_machine.no_quarter_state
        else:
            print("Oops, out of gumballs!")
            self.gumball_machine.state = self.gumball_machine.sold_out_state

    def refill(self) -> None:
        pass

    def __str__(self) -> str:
        return "dispensing a gumball"


class WinnerState:
    def __init__(self, gumball_machine: GumballMachine) -> None:
        self.gumball_machine = gumball_machine

    def insert_quarter(self) -> None:
        print("Please wait, we're already giving you a Gumball")

    def eject_quarter(self) -> None:
        print("Please wait, we're already giving you a Gumball")

    def turn_crank(self) -> None:
        print("Turning twice doesn't get you another gumball!")

    def dispense(self) -> None:
        self.gumball_machine.release_ball()
        if self.gumball_machine.count == 0:
            self.gumball_machine.state = self.gumball_machine.sold_out_state
        else:
            self.gumball_machine.release_ball()
            print("YOU'RE A WINNER! You got two gumballs for your quarter")
            if self.gumball_machine.count > 0:
                self.gumball_machine.state = self.gumball_machine.no_quarter_state
            else:
                print("Oops, out of gumballs!")
                self.gumball_machine.state = self.gumball_machine.sold_out_state

    def refill(self) -> None:
        pass

    def __str__(self) -> str:
        return "despensing two gumballs for your quarter, because YOU'RE A WINNER!"


def main() -> None:
    gumball_machine = GumballMachine(10)
    print(gumball_machine)

    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()

    print(gumball_machine)

    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()

    print(gumball_machine)

    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()

    print(gumball_machine)

    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()

    print(gumball_machine)

    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()

    print(gumball_machine)


if __name__ == "__main__":
    main()
