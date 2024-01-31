# formula: min(a, b) * (b_i - a_i)
# [7, 1, 2, 3, 9], length = 7, width = 4, answer = 28
# [], answer = 0
# [5], answer = 0
# [6, 9, 3, 4, 5, 8], length = 8, width = 4, answer = 32. (9-8 > 6-8)
# [4, 5, 1, 6, 3], length = 3, width = 4, answer = 12


# T: O(n**2), S: O(1)
def get_max_water_container(heights):
    max_area = 0
    for i in range(len(heights)):
        for j in range(i + 1, len(heights)):
            max_area = max(max_area, min(heights[j], heights[i]) * (j - i))
    return max_area


# T: O(n), S: O(1)
def get_max_water_container_2p(heights):
    max_area = 0
    left, right = 0, len(heights) - 1
    while left < right:
        max_area = max(max_area, min(heights[right], heights[left]) * (right - left))
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return max_area


if __name__ == "__main__":
    inputs = [
        [7, 1, 2, 3, 9],
        [],
        [5],
        [6, 9, 3, 4, 5, 8],
        [4, 5, 1, 6, 3],
    ]
    for heights in inputs:
        print(get_max_water_container(heights))
        print(get_max_water_container_2p(heights))
