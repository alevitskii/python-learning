# [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2], answer = 8
# [], answer = 0
# [3], answer = 0
# [3, 4, 3], answer = 0

# formula: cW = min(maxL, maxR) - cH


# T: O(n**2), S: O(1)
def get_trapped_water(heights):
    total = 0
    for i in range(len(heights)):
        left, right = i, i
        max_left, max_right = 0, 0

        while left >= 0:
            max_left = max(max_left, heights[left])
            left -= 1
        while right < len(heights):
            max_right = max(max_right, heights[right])
            right += 1

        area = min(max_left, max_right) - heights[i]
        if area > 0:  # can be negative
            total += area

    return total


# T: O(n), S: O(1)
def get_trapped_water_2p(heights):
    total = 0
    max_left, max_right = 0, 0
    left_index, right_index = 0, len(heights) - 1

    while left_index < right_index:
        if heights[left_index] <= heights[right_index]:
            if heights[left_index] < max_left:
                total += max_left - heights[left_index]
            else:
                max_left = heights[left_index]
            left_index += 1
        else:
            if heights[right_index] < max_right:
                total += max_right - heights[right_index]
            else:
                max_right = heights[right_index]
            right_index -= 1

    return total


if __name__ == "__main__":
    inputs = [
        [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2],
        [],
        [3],
        [3, 4, 3],
    ]
    for heights in inputs:
        print(get_trapped_water(heights))
        print(get_trapped_water_2p(heights))
