from typing import List


class Solution:
    def binary_search(self, jobs, right, cutoff):
        left = 0
        while left < right:
            mid = (left + right) >> 1
            if jobs[mid][1] <= cutoff:
                left = mid + 1
            else:
                right = mid
        return left

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort(key=lambda i: i[1])
        dp = [0] * (len(jobs) + 1)
        for idx, job in enumerate(jobs, start=1):
            not_take = dp[idx - 1]
            non_overlapping_idx = self.binary_search(jobs, idx - 1, job[0])
            take = dp[non_overlapping_idx] + job[2]
            dp[idx] = max(take, not_take)
        return dp[-1]


class Solution2:
    def binary_search(self, jobs, current_job):
        left = 0
        right = current_job - 1
        prev_valid_index = -1
        while left <= right:
            mid = (left + right) // 2
            if jobs[mid][1] <= jobs[current_job][0]:
                prev_valid_index = mid
                left = mid + 1
            else:
                right = mid - 1
        return prev_valid_index

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = zip(startTime, endTime, profit)
        jobs = sorted(jobs, key=lambda x: x[1])
        n = len(jobs)
        dp = [0] * n
        for i in range(n):
            included_profit = jobs[i][2]
            prev_valid_job = self.binary_search(jobs, i)
            if prev_valid_job != -1:
                included_profit += dp[prev_valid_job]
            if i > 0:
                excluded_profit = dp[i - 1]
            else:
                excluded_profit = 0
            dp[i] = max(included_profit, excluded_profit)
        return dp[n - 1]


def main() -> None:
    inputs = [
        ([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]),
        ([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60]),
        ([1, 1, 1], [2, 3, 4], [5, 6, 4]),
    ]
    s = Solution2()
    for startTime, endTime, profit in inputs:
        print(s.jobScheduling(startTime, endTime, profit))


if __name__ == "__main__":
    main()
