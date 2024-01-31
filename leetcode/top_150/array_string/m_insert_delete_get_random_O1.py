from random import randint


class RandomizedSet:
    def __init__(self):
        self._list = []
        self._dict = {}

    def insert(self, val: int) -> bool:
        if val in self._dict:
            return False
        self._list.append(val)
        self._dict[val] = len(self._list) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self._dict:
            return False
        remove_idx = self._dict[val]
        self._list[remove_idx], self._list[-1] = self._list[-1], self._list[remove_idx]
        self._dict[self._list[remove_idx]] = remove_idx
        # self._list.pop()
        del self._dict[self._list.pop()]
        return True

    def getRandom(self) -> int:
        idx = randint(0, len(self._list) - 1)
        return self._list[idx]


if __name__ == "__main__":
    rand_set = RandomizedSet()
    print(rand_set.insert(1))
    print(rand_set.remove(2))
    print(rand_set.insert(2))
    print(rand_set.getRandom())
    print(rand_set.remove(1))
    print(rand_set.insert(2))
    print(rand_set.getRandom())
