# "abccabb", answer = 3
# "cccccc", answer = 1
# "", answer = 0
# "abccbda", answer = 4


# T: O(n**2), S: O(n)
def length_of_longest_substring(string):
    if len(string) <= 1:
        return len(string)
    longest = 0
    for i in range(len(string)):
        seen_chars = set()
        current_length = 0
        for j in range(i, len(string)):
            if string[j] not in seen_chars:
                current_length += 1
                seen_chars.add(string[j])
                longest = max(longest, current_length)
            else:
                break
    return longest


# T: O(n), S: O(n)
def length_of_longest_substring_p(string):
    if len(string) <= 1:
        return len(string)
    longest = 0
    left, right = 0, 0
    seen_chars = {}
    for right in range(len(string)):
        current_char = string[right]
        prev_seen_char = seen_chars.get(current_char, -1)
        if prev_seen_char >= left:
            left = prev_seen_char + 1
        seen_chars[current_char] = right
        longest = max(longest, right - left + 1)
    return longest


if __name__ == "__main__":
    inputs = [
        "abccabb",
        "cccccc",
        "",
        "abccbda",
    ]
    for string in inputs:
        print(length_of_longest_substring(string))
        print(length_of_longest_substring_p(string))
