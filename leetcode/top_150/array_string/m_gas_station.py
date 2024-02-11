from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        tank, idx = 0, 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank, idx = 0, i + 1
        return idx


def main() -> None:
    inputs = [
        ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]),
        ([2, 3, 4], [3, 4, 3]),
    ]
    s = Solution()
    for gas, cost in inputs:
        print(s.canCompleteCircuit(gas, cost))


if __name__ == "__main__":
    main()
