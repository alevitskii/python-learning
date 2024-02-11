from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return left + 1, right + 1
            elif s < target:
                left += 1
            else:
                right -= 1


def main() -> None:
    inputs = [
        ([2, 7, 11, 15], 9),
        ([2, 3, 4], 6),
        ([-1, 0], -1),
    ]
    s = Solution()
    for numbers, target in inputs:
        print(s.twoSum(numbers, target))


if __name__ == "__main__":
    main()
