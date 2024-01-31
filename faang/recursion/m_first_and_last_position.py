# T: O(logn), S: O(1) with tail recursion
def binary_search_rec(array, left, right, target):
    if left > len(array) - 1 or right < 0:
        return None
    mid = (right + left) // 2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search_rec(array, mid + 1, right, target)
    else:
        return binary_search_rec(array, left, mid - 1, target)


# T: O(logn), S: O(1)
def binary_search_iter(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (right + left) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return


# [1, 3, 3, 5, 5, 8, 9], 5 => [3, 5]
# [1, 2, 3, 4, 5, 6], 4 => [3, 3]
# [1, 2, 3, 4, 5], 9 => [-1, -1]
# [], _ => [-1, -1]


# T: O(logn), S: O(1)
def get_first_and_last_position(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (right + left) // 2
        if array[mid] == target:
            result = [None, None]
            sub_left, sub_right = left, mid - 1
            while sub_left <= sub_right:
                sub_mid = (sub_right + sub_left) // 2
                if array[sub_mid] != target:
                    sub_left = sub_mid + 1
                else:
                    sub_right = sub_mid - 1
            result[0] = sub_left

            sub_left, sub_right = mid + 1, right
            while sub_left <= sub_right:
                sub_mid = (sub_right + sub_left) // 2
                if array[sub_mid] != target:
                    sub_right = sub_mid - 1
                else:
                    sub_left = sub_mid + 1
            result[1] = sub_right

            return result
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return [-1, -1]


if __name__ == "__main__":
    inputs = [
        ([1, 3, 3, 5, 5, 8, 9], 5),
        ([1, 2, 3, 4, 5, 6], 4),
        ([1, 2, 3, 4, 5], 9),
        ([], 1),
    ]
    for array, target in inputs:
        # print(binary_search_rec(array, 0, len(array)-1, target))
        # print(binary_search_iter(array, target))
        print(get_first_and_last_position(array, target))
