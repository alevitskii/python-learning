from dataclasses import dataclass, field


@dataclass
class Member:
    name: str
    alive: bool = True


class Monarchy:
    def __init__(self, king) -> None:
        self.king = king
        self.members = {king: Member(king)}
        self.tree = {king: []}

    def birth(self, child, parent) -> None:
        self.members[child] = Member(child)
        self.tree[parent].append(child)
        self.tree[child] = []

    def death(self, member):
        self.members[member].alive = False

    def _traverse_pre_order(self, member, order):
        if self.members[member].alive:
            order.append(member)
        for child in self.tree[member]:
            self._traverse_pre_order(child, order)

    def get_order_of_succession(self) -> list[str]:
        order = []
        self._traverse_pre_order(self.king, order)
        return order


@dataclass
class Person:
    name: str
    alive: bool = True
    children: list = field(default_factory=list)


class Monarchy2:
    def __init__(self, king) -> None:
        self.king = Person(king)
        self._persons = {self.king.name: self.king}

    def birth(self, child, parent) -> None:
        self._persons[child] = Person(child)
        self._persons[parent].children.append(self._persons[child])

    def death(self, person):
        if person in self._persons:
            self._persons[person].alive = False

    def _traverse_pre_order(self, person: Person, order):
        if person.alive:
            order.append(person.name)
        for child in person.children:
            self._traverse_pre_order(child, order)

    def get_order_of_succession(self) -> list[str]:
        order = []
        self._traverse_pre_order(self.king, order)
        return order


if __name__ == "__main__":
    monarchy = Monarchy("Jake")
    monarchy.birth("Catherine", "Jake")
    monarchy.birth("Jane", "Catherine")
    monarchy.birth("Farah", "Jane")
    monarchy.birth("Tom", "Jake")
    monarchy.birth("Celine", "Jake")
    monarchy.birth("Mark", "Catherine")
    monarchy.birth("Peter", "Celine")
    print(monarchy.get_order_of_succession())
    monarchy.death("Jake")
    monarchy.death("Jane")
    print(monarchy.get_order_of_succession())

    monarchy = Monarchy2("Jake")
    monarchy.birth("Catherine", "Jake")
    monarchy.birth("Jane", "Catherine")
    monarchy.birth("Farah", "Jane")
    monarchy.birth("Tom", "Jake")
    monarchy.birth("Celine", "Jake")
    monarchy.birth("Mark", "Catherine")
    monarchy.birth("Peter", "Celine")
    print(monarchy.get_order_of_succession())
    monarchy.death("Jake")
    monarchy.death("Jane")
    print(monarchy.get_order_of_succession())
