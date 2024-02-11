from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_length = 0
        while s:
            n = s.pop()
            length = 1
            l, r = n, n
            while r + 1 in s:
                length += 1
                s.remove(r + 1)
                r += 1
            while l - 1 in s:
                length += 1
                s.remove(l - 1)
                l -= 1
            max_length = max(max_length, length)
        return max_length


class Solution2:
    def find(self, idx, parent):
        if parent[idx] != idx:
            parent[idx] = self.find(parent[idx], parent)
        return parent[idx]

    def union(self, idx1, idx2, parent, size):
        ridx1 = self.find(idx1, parent)
        ridx2 = self.find(idx2, parent)
        if ridx1 != ridx2:
            if size[ridx1] <= size[ridx2]:
                parent[ridx1] = ridx2
                size[ridx2] += size[ridx1]
            else:
                parent[ridx2] = ridx1
                size[ridx1] += size[ridx2]

    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        parent = list(range(len(nums)))
        size = [1] * len(nums)
        hash_map = {v: i for i, v in enumerate(nums)}
        for n in nums:
            if n - 1 in hash_map:
                self.union(hash_map[n - 1], hash_map[n], parent, size)
            if n + 1 in hash_map:
                self.union(hash_map[n + 1], hash_map[n], parent, size)
        return max(size)


def main() -> None:
    inputs = [[100, 4, 200, 1, 3, 2], [0, 3, 7, 2, 5, 8, 4, 6, 0, 1], [78, 2, 32, 4, 1, 3], [], [1, 2]]
    s = Solution2()
    for nums in inputs:
        print(s.longestConsecutive(nums))


if __name__ == "__main__":
    main()
