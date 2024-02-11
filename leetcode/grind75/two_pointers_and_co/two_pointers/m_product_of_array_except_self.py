from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        pre, post = 1, 1
        for i in range(len(nums)):
            answer[i] *= pre
            pre = pre * nums[i]
            answer[-i - 1] *= post
            post = post * nums[-i - 1]
        return answer


class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        left_product, right_product = 1, 1
        left = 0
        right = n - 1

        while left < n and right > -1:
            res[left] *= left_product
            res[right] *= right_product

            left_product *= nums[left]
            right_product *= nums[right]

            left += 1
            right -= 1

        return res


def main() -> None:
    inputs = [
        [1, 2, 3, 4],
        [-1, 1, 0, -3, 3],
    ]

    s = Solution2()
    for nums in inputs:
        print(s.productExceptSelf(nums))


if __name__ == "__main__":
    main()
