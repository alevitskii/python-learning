from typing import List


# https://ru.wikipedia.org/wiki/Алгоритм_большинства_голосов_Бойера_—_Мура
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        for i in nums:
            if count == 0:
                candidate = i
            count += 1 if candidate == i else -1
        return candidate


def main() -> None:
    inputs = [
        [2, 2, 1, 1, 1, 2, 2],
    ]
    s = Solution()
    for nums in inputs:
        print(s.majorityElement(nums))


if __name__ == "__main__":
    main()
