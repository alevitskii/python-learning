import re

# "aabaa", answer = True
# "aabbaa", answer = True
# "abc", answer = False
# "a", answer = True
# "", answer = True
# "A man, a plan, a canal: Panama", answer = True


def is_valid_palindrome_edges(string: str):
    if len(string) <= 1:
        return True
    string = re.sub(r"[^A-Za-z0-9]+", "", string).lower()
    left, right = 0, len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True


def is_valid_palindrome_center(string: str):
    if len(string) <= 1:
        return True
    string = re.sub(r"[^A-Za-z0-9]+", "", string).lower()
    left = (len(string) - 1) // 2
    right = left + 1 if len(string) % 2 == 0 else left
    while left >= 0 and right < len(string):
        if string[left] != string[right]:
            return False
        left -= 1
        right += 1
    return True


def is_valid_palindrome_reverse(string: str):
    if len(string) <= 1:
        return True
    string = re.sub(r"[^A-Za-z0-9]+", "", string).lower()
    rev = list(reversed(string))
    for i in range(len(string)):
        if string[i] != rev[i]:
            return False
    return True


if __name__ == "__main__":
    inputs = ["aabaa", "aabbaa", "abc", "a", "", "A man, a plan, a canal: Panama"]
    for string in inputs:
        print(is_valid_palindrome_edges(string))
        print(is_valid_palindrome_center(string))
        print(is_valid_palindrome_reverse(string))
