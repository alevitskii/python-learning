from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self) -> str:
        node = self
        s = ""
        while node:
            s += f"{node.val} --> "
            node = node.next
        return s + "None"


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None

    def _move_to_top(self, node):
        if node == self.head:
            return
        elif node == self.tail:
            self.tail = node.prev
            self.tail.next = None
            node.prev = None
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = self.head
            node.prev = None
            self.head.prev = node
            self.head = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_top(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._move_to_top(node)
        else:
            if len(self.cache) == self.capacity:
                del self.cache[self.tail.key]
                self.tail = self.tail.prev
                if self.tail:
                    self.tail.next = None
            node = ListNode(key=key, val=value, next=self.head)
            if self.head is not None:
                self.head.prev = node
            self.head = node
            if self.tail is None:
                self.tail = self.head
            self.cache[key] = node


if __name__ == "__main__":
    # lRUCache = LRUCache(2)
    # print(lRUCache.put(1, 1))  # cache is {1=1}
    # print(lRUCache.put(2, 2))  # cache is {1=1, 2=2}
    # print(lRUCache.get(1))     # return 1
    # print(lRUCache.put(3, 3))  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    # print(lRUCache.get(2))     # returns -1 (not found)
    # print(lRUCache.put(4, 4))  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    # print(lRUCache.get(1))     # return -1 (not found)
    # print(lRUCache.get(3))     # return 3
    # print(lRUCache.get(4))     # return 4

    lRUCache = LRUCache(1)
    print(lRUCache.put(2, 1))  # cache is {1=1}
    print(lRUCache.get(2))  # return 1
    print(lRUCache.put(3, 2))  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    print(lRUCache.get(2))  # returns -1 (not found)
    print(lRUCache.get(3))  # return -1 (not found)
