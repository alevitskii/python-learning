class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # Initialize a variable 'shift' to 0.
        shift = 0
        print("left:", left, bin(left), "right:", right, bin(right))
        # While the left and right limits are not equal,
        while left < right:
            # Right shift the left limit by 1 bit.
            left >>= 1
            # Right shift the right limit by 1 bit.
            right >>= 1
            # Increment the 'shift' variable by 1.
            shift += 1
            print("left:", left, bin(left), "right:", right, bin(right))
        print(f"left shifted by {shift}", bin(left << shift))
        # Left shift the left limit by 'shift' bits and return the result.
        return left << shift


def main() -> None:
    inputs = [
        (5, 7),
        # (0, 0),
        # (1, 2147483647),
        # (600000000, 2147483645),
    ]
    s = Solution()
    for left, right in inputs:
        print(s.rangeBitwiseAnd(left, right))


if __name__ == "__main__":
    main()
