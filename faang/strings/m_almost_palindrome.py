# "raceacar", answer = True
# "abccdba", answer = True
# "abcdefdba", answer = False
# "", answer = True
# "a", answer = True
# "ab", answer = True


def is_valid_palindrome(string, left, right):
    if len(string) <= 1:
        return True
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True


# T: ~O(n), S: O(1)
def is_almost_palindrome(string):
    left, right = 0, len(string) - 1

    while left < right:
        if string[left] != string[right]:
            return is_valid_palindrome(string, left + 1, right) or is_valid_palindrome(string, left, right - 1)
        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    inputs = ["raceacar", "abccdba", "abcdefdba", "", "a", "ab"]
    for string in inputs:
        print(is_almost_palindrome(string))
