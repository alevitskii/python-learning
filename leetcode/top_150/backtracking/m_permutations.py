from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recursive(src, perm):
            if len(src) == 0:
                result.append(perm.copy())
                return
            for i in range(len(src)):
                perm.append(src[i])
                recursive(src[:i] + src[i + 1 :], perm)
                perm.pop()

        result = []
        recursive(nums, [])
        return result


def main() -> None:
    inputs = [
        [1, 2, 3],
        [0, 1],
        [1],
    ]
    s = Solution()
    for nums in inputs:
        print(s.permute(nums))


if __name__ == "__main__":
    main()
