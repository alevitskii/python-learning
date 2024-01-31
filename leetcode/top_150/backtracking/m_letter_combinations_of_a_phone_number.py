from typing import List

MAPPING = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def combine(current, digits):
            if len(digits) == 0:
                return current
            digit = digits[0]
            for letter in MAPPING[digit]:
                combination = combine(current + letter, digits[1:])
                if combination is not None:
                    result.append(combination)

        result = []
        combine("", digits)
        return result


class Solution2:
    def letterCombinations(self, digits: str) -> List[str]:
        def combine(current, digits):
            if len(digits) == 0:
                result.append(current)
                return
            digit = digits[0]
            for letter in MAPPING[digit]:
                combine(current + letter, digits[1:])

        result = []
        combine("", digits)
        return result


if __name__ == "__main__":
    inputs = ["23", "", "2"]
    s = Solution()
    for digits in inputs:
        print(s.letterCombinations(digits))
