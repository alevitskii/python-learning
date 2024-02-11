from collections import deque
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        product = 1
        for i in range(len(nums) - 1):
            product *= nums[i]
            answer[i + 1] *= product
        product = 1
        for i in range(len(nums) - 1, 0, -1):
            product *= nums[i]
            answer[i - 1] *= product
        return answer


class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [1] * length
        left_product, right_product = 1, 1

        for i in range(length - 1):
            left_product *= nums[i]
            answer[i + 1] *= left_product
            right_product *= nums[length - 1 - i]
            answer[length - 2 - i] *= right_product
        return answer


def main() -> None:
    inputs = [[1, 2, 3, 4], [-1, 1, 0, -3, 3], [2, 3, 4, 5, 6, 7], [1], [1, 2, 3]]
    s = Solution2()
    for nums in inputs:
        print(s.productExceptSelf(nums))


if __name__ == "__main__":
    main()
