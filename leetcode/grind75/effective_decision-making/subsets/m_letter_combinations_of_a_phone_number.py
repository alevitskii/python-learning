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


class Solution3:
    def backtrack(self, index, path, digits, combinations):
        if len(path) == len(digits):
            combinations.append("".join(path))
            return
        possible_letters = MAPPING[digits[index]]
        if possible_letters:
            for letter in possible_letters:
                path.append(letter)
                self.backtrack(index + 1, path, digits, combinations)
                path.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        combinations = []
        if len(digits) == 0:
            return []
        self.backtrack(0, [], digits, combinations)
        return combinations


def main() -> None:
    inputs = ["23", "", "2"]
    s = Solution2()
    for digits in inputs:
        print(s.letterCombinations(digits))


if __name__ == "__main__":
    main()
