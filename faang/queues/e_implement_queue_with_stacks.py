# S: O(n)
class Queue:
    def __init__(self) -> None:
        self.push_stack = []
        self.pop_stack = []

    # T: O(1)
    def enqueue(self, value):
        self.push_stack.append(value)

    # T: O(n)
    def dequeue(self):
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


if __name__ == "__main__":
    queue = Queue()
    print(queue.enqueue(1))
    print(queue.enqueue(2))
    print(queue.enqueue(3))
    print(queue.dequeue())
    print(queue.peek())
    print(queue.empty())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.empty())
