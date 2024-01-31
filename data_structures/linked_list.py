class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class Singly:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        self.tail.next = Node(value)
        self.tail = self.tail.next
        self.length += 1

    def prepend(self, value):
        self.head = Node(value, self.head)
        self.length += 1

    def lookup(self, index):
        idx = 0
        node = self.head
        while idx != index:
            node = node.next
            idx += 1
        return node

    def insert(self, index, value):
        if index == 0:
            self.prepend(value)
            return
        if index >= self.length:
            self.append(value)
            return

        leader = self.lookup(index - 1)
        node = Node(value, leader.next)
        leader.next = node
        self.length += 1

    def remove(self, index):
        if index >= self.length:
            return
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return
        node = self.lookup(index - 1)
        node.next = node.next.next
        if index == self.length - 1:
            self.tail = node
        self.length -= 1

    def reverse(self):
        if self.head.next is None:
            return
        first = self.head
        self.tail = self.head
        second = first.next
        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp
        self.head.next = None
        self.head = first

    def create_reversed(self):
        current = Node(self.head.value)
        node = self.head
        while node.next:
            new_node = Node(node.next.value, current)
            current = new_node
            node = node.next
        return current

    def __str__(self, start=None):
        node = start or self.head
        result = ""
        while node:
            result += str(node.value) + " --> "
            node = node.next
        return result + "None"


class Doubly:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        self.tail.next = Node(value, prev=self.tail)
        self.tail = self.tail.next
        self.length += 1

    def prepend(self, value):
        node = Node(value, next=self.head)
        self.head.prev = node
        self.head = node
        self.length += 1

    def lookup(self, index):
        idx = 0
        node = self.head
        while idx != index:
            node = node.next
            idx += 1
        return node

    def insert(self, index, value):
        if index == 0:
            self.prepend(value)
            return
        if index >= self.length:
            self.append(value)
            return

        leader = self.lookup(index - 1)
        node = Node(value, next=leader.next, prev=leader)
        leader.next.prev = node
        leader.next = node
        self.length += 1

    def remove(self, index):
        if index >= self.length:
            return
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return
        node = self.lookup(index)
        if node.next:
            node.next.prev = node.prev
        node.prev.next = node.next
        if index == self.length - 1:
            self.tail = node.prev
        self.length -= 1

    def __str__(self):
        straight = ""
        node = self.head
        while node:
            straight += str(node.value) + " --> "
            node = node.next
        straight += "None"

        backwards = "None"
        node = self.tail
        while node:
            backwards += " <-- " + str(node.value)
            node = node.prev
        return straight + "\n" + backwards


if __name__ == "__main__":
    ll = Singly(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.insert(2, 99)
    print(ll)
    ll.remove(4)
    print(ll)
    print(ll.head.value)
    print(ll.tail.value)
    print(ll.__str__(ll.create_reversed()))
    ll.reverse()
    print(ll)
    # ll = Doubly(1)
    # ll.append(2)
    # ll.append(3)
    # ll.append(4)
    # ll.prepend(10)
    # ll.insert(2, 99)
    # ll.remove(2)
    # ll.remove(4)
    # ll.remove(0)
    # print(ll)
    # print(ll.head.value)
    # print(ll.taill.value)
    # print(ll.length)
