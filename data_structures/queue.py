class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next


class Queue:
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first

    def enqueue(self, value):
        node = Node(value)
        if self.length == 0:
            self.first = self.last = node
        else:
            self.last.next = node
            self.last = node
        self.length += 1

    def dequeue(self):
        if self.first is None:
            return None
        if self.first == self.last:
            self.last = None
        node = self.first
        self.first = self.first.next
        self.length -= 1
        return node

    def __str__(self) -> str:
        node = self.first
        result = ""
        while node:
            result += str(node.value) + " --> "
            node = node.next
        return result + "None"


def main() -> None:
    queue = Queue()
    queue.enqueue("1")
    queue.enqueue("2")
    queue.enqueue("3")
    print(queue)
    print(queue.peek().value)
    queue.dequeue()
    print(queue)


if __name__ == "__main__":
    main()
