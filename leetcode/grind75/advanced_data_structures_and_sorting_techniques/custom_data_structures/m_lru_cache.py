from m_lru_cache_helper import LinkedList


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


class LRUCache2:
    # Initializes an LRU cache with the capacity size
    def __init__(self, capacity):
        self.cache_capacity = capacity
        self.cache_map = {}
        self.cache_list = LinkedList()

    # Returns the value of the key, or -1 if the key does not exist.
    def get(self, key):
        found_itr = None
        if key in self.cache_map:
            found_itr = self.cache_map[key]
        else:
            return -1

        list_iterator = found_itr
        self.cache_list.move_to_head(found_itr)

        return list_iterator.pair[1]

    # Adds a new key-value pair or updates an existing key with a new value
    def set(self, key, value):
        if key in self.cache_map:
            found_iter = self.cache_map[key]
            list_iterator = found_iter
            self.cache_list.move_to_head(found_iter)
            list_iterator.pair[1] = value
            return

        if len(self.cache_map) == self.cache_capacity:
            key_tmp = self.cache_list.get_tail().pair[0]
            self.cache_list.remove_tail()
            del self.cache_map[key_tmp]

        self.cache_list.insert_at_head([key, value])
        self.cache_map[key] = self.cache_list.get_head()

    def print(self):
        print("Cache current size: ", self.cache_list.size, ", ", end="")
        print("Cache contents: {", end="")
        node = self.cache_list.get_head()
        while node:
            print("{", str(node.pair[0]), ",", str(node.pair[1]), "}", end="")
            node = node.next
            if node:
                print(", ", end="")
        print("}")
        print("-" * 100, "\n")


def main() -> None:
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


if __name__ == "__main__":
    main()
