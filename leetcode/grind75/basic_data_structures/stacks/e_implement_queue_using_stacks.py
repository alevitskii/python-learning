class MyQueue:
    def __init__(self) -> None:
        self.push_stack = []
        self.pop_stack = []

    # T: O(1)
    def push(self, value):
        self.push_stack.append(value)

    # T: O(n)
    def pop(self):
        if self.peek():
            return self.pop_stack.pop()
        return

    # T: O(n)
    def peek(self):
        if not self.pop_stack:
            self.pop_stack, self.push_stack = self.push_stack[::-1], []
        return self.pop_stack[-1] if self.pop_stack else None

    # T: O(n)
    def empty(self):
        return self.peek() is None


def main() -> None:
    obj = MyQueue()
    print(obj.push(1))
    print(obj.pop())
    print(obj.peek())
    print(obj.empty())


if __name__ == "__main__":
    main()
