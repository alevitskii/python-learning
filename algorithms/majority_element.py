# Boyer-Moore’s voting algorithm
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = -1
        count = 0
        for n in nums:
            if count == 0:
                candidate = n
            count += 1 if n == candidate else -1
        return candidate


def main() -> None:
    inputs = [
        [3, 2, 3],
        [2, 2, 1, 1, 1, 2, 2],
    ]
    s = Solution()
    for nums in inputs:
        print(s.majorityElement(nums))


if __name__ == "__main__":
    main()
