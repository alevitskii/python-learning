from typing import List


class Solution:
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


class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()

        n, p, z = [], [], 0
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z += 1

        N, P = set(n), set(p)

        if z:
            for num in P:
                if -num in N:
                    res.add((-num, 0, num))
        if z >= 3:
            res.add((0, 0, 0))

        for lst, L in [(n, P), (p, N)]:
            for i in range(len(lst)):
                for j in range(i + 1, len(lst)):
                    target = -(lst[i] + lst[j])
                    if target in L:
                        res.add(tuple(sorted([lst[i], lst[j], target])))

        return res


if __name__ == "__main__":
    inputs = [[-1, 0, 1, 2, -1, -4], [0, 1, 1], [0, 0, 0]]

    s = Solution()
    for nums in inputs:
        print(s.threeSum(nums))
