from typing import List


# Timeout
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def two_sum(start, target):
            nonlocal nums
            d = {}
            res = []
            for i in range(start, len(nums)):
                if nums[i] in d:
                    for idx in d[nums[i]]:
                        res.append((i, idx))
                temp = target - nums[i]
                if temp not in d:
                    d[temp] = []
                d[temp].append(i)
            return res

        res = set()
        for i in range(len(nums)):
            r = two_sum(i + 1, 0 - nums[i])
            for e in r:
                res.add(tuple(sorted([nums[i], nums[e[0]], nums[e[1]]])))
        return res


class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        posset, negset = set(), set()
        poslist, neglist = [], []
        res = set()
        zeroes_cnt = 0
        for n in nums:
            if n == 0:
                zeroes_cnt += 1
            if n < 0:
                neglist.append(n)
                negset.add(n)
            else:
                poslist.append(n)
                posset.add(n)
        if zeroes_cnt > 2:
            res.add((0, 0, 0))
        for i in range(len(poslist)):
            for j in range(i + 1, len(poslist)):
                if -(poslist[i] + poslist[j]) in negset:
                    res.add(tuple(sorted([poslist[i], poslist[j], -(poslist[i] + poslist[j])])))
            if -poslist[i] in negset and zeroes_cnt > 0:
                res.add(tuple(sorted([-poslist[i], 0, poslist[i]])))
        for i in range(len(neglist)):
            for j in range(i + 1, len(neglist)):
                if -(neglist[i] + neglist[j]) in posset:
                    res.add(tuple(sorted([neglist[i], neglist[j], -(neglist[i] + neglist[j])])))
            if -neglist[i] in posset and zeroes_cnt > 0:
                res.add(tuple(sorted([-neglist[i], 0, neglist[i]])))
        return res


if __name__ == "__main__":
    inputs = [[-1, 0, 1, 2, -1, -4], [0, 1, 1], [0, 0, 0], [-1, 0, 1, 0]]
    s = Solution2()
    for nums in inputs:
        print(s.threeSum(nums))
