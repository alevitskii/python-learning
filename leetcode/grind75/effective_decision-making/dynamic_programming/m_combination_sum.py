from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(current, i, total):
            if total == target:
                result.append(current.copy())
                return
            elif total > target or i >= len(candidates):
                return
            current.append(candidates[i])
            dfs(current, i, total + candidates[i])
            current.pop()
            dfs(current, i + 1, total)

        result = []
        dfs([], 0, 0)
        return result


class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]
        dp[0].append([])
        for i in range(1, target + 1):
            for j in range(len(candidates)):
                if candidates[j] <= i:
                    for prev in dp[i - candidates[j]]:
                        temp = prev + [candidates[j]]
                        temp.sort()
                        if temp not in dp[i]:
                            dp[i].append(temp)
        return dp[target]


if __name__ == "__main__":
    inputs = [
        ([2, 3, 6, 7], 7),
        ([2, 3, 5], 8),
        ([2], 1),
    ]

    s = Solution2()
    for candidates, target in inputs:
        print(s.combinationSum(candidates, target))
