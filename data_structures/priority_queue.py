import math


class PriorityQueue:
    def __init__(self, comparator=lambda a, b: a > b) -> None:
        self._heap = []
        self._comparator = comparator

    def size(self):
        return len(self._heap)

    def is_empty(self):
        return self.size() == 0

    def peek(self):
        return self._heap[0] if not self.is_empty() else None

    def push(self, value):
        self._heap.append(value)
        self._sift_up()
        return self.size()

    def _sift_up(self):
        node_idx = self.size() - 1
        parent_idx = self._parent(node_idx)
        while node_idx > 0 and self._compare(node_idx, parent_idx):
            self._swap(node_idx, parent_idx)
            node_idx = parent_idx
            parent_idx = self._parent(node_idx)

    def pop(self):
        if self.size() > 1:
            self._swap(0, self.size() - 1)
        popped_value = self._heap.pop()
        self._sift_down()
        return popped_value

    def _sift_down(self):
        node_idx = 0
        while (self._left_child(node_idx) < self.size() and self._compare(self._left_child(node_idx), node_idx)) or (
            self._right_child(node_idx) < self.size() and self._compare(self._right_child(node_idx), node_idx)
        ):
            greater_child_idx = (
                self._right_child(node_idx)
                if self._right_child(node_idx) < self.size()
                and self._compare(self._right_child(node_idx), self._left_child(node_idx))
                else self._left_child(node_idx)
            )
            self._swap(greater_child_idx, node_idx)
            node_idx = greater_child_idx

    def _parent(self, idx):
        return math.floor((idx - 1) / 2)

    def _left_child(self, idx):
        return idx * 2 + 1

    def _right_child(self, idx):
        return idx * 2 + 2

    def _swap(self, i, j):
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def _compare(self, i, j):
        return self._comparator(self._heap[i], self._heap[j])


if __name__ == "__main__":
    main()
