from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for idx in range(len(digits) - 1, -1, -1):
            if digits[idx] < 9:
                digits[idx] += 1
                return digits
            else:
                digits[idx] = 0
        return [1] + digits


if __name__ == "__main__":
    inputs = [[1, 2, 3], [4, 3, 2, 1], [9], [9, 9, 9]]
    s = Solution()
    for digits in inputs:
        print(s.plusOne(digits))
