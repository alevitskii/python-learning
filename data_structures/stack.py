class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next


class Stack:
    def __init__(self) -> None:
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top

    def push(self, value):
        node = Node(value, self.top)
        self.top = node
        if self.length == 0:
            self.bottom = node
        self.length += 1

    def pop(self):
        if self.top is None:
            return None
        if self.top == self.bottom:
            self.bottom = None
        node = self.top
        self.top = self.top.next
        self.length -= 1
        return node

    def __str__(self) -> str:
        node = self.top
        result = ""
        while node:
            result += str(node.value) + " --> "
            node = node.next
        return result + "None"


class StackArray:
    def __init__(self) -> None:
        self.array = []

    def peek(self):
        return self.array[-1] if len(self.array) > 0 else None

    def push(self, value):
        self.array.append(value)

    def pop(self):
        return self.array.pop()

    def __str__(self) -> str:
        return " --> ".join(self.array)


if __name__ == "__main__":
    # stack = Stack()
    # stack.push(1)
    # stack.push(2)
    # stack.push(3)
    # print(stack.peek().value)
    # stack.pop()
    # # stack.pop()
    # print(stack)
    # print(stack.top.value)
    # print(stack.bottom.value)
    stack = StackArray()
    stack.push("1")
    stack.push("2")
    stack.push("3")
    print(stack.peek())
    stack.pop()
    # stack.pop()
    print(stack)
