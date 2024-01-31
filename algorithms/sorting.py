def bubble_sort(array):
    first, swap = True, True
    while swap or first:
        first, swap = False, False
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i + 1], array[i] = array[i], array[i + 1]
                swap = True


def selection_sort(array):
    length = len(array)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]


# good when a short array is nearly sorted
def insertion_sort(array):
    length = len(array)
    for i in range(length):
        if array[0] > array[i]:
            array = [array[i]] + array[:i] + array[i + 1 :]
        else:
            for j in range(1, i):
                if array[j - 1] < array[i] < array[j]:
                    array = array[:j] + [array[i]] + array[j:i] + array[i + 1 :]

    return array


def merge(left, right):
    merged = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


def merge_sort(array):
    if len(array) == 1:
        return array

    left, right = array[: len(array) // 2], array[len(array) // 2 :]

    return merge(merge_sort(left), merge_sort(right))


def quick_sort_right(array):
    if len(array) <= 1:
        return array

    pivot_index = len(array) - 1
    index = 0
    while index < pivot_index:
        if array[index] > array[pivot_index]:
            array[index], array[pivot_index - 1], array[pivot_index] = (
                array[pivot_index - 1],
                array[pivot_index],
                array[index],
            )
            pivot_index -= 1
        else:
            index += 1

    return quick_sort_right(array[:pivot_index]) + [array[pivot_index]] + quick_sort_right(array[pivot_index + 1 :])


def quick_sort_left(nums):
    if len(nums) <= 1:
        return nums

    index, pivot_index = 0, 0
    while index < len(nums):
        if nums[index] < nums[-1]:
            nums[pivot_index], nums[index] = nums[index], nums[pivot_index]
            index += 1
            pivot_index += 1
        else:
            index += 1
    nums[pivot_index], nums[-1] = nums[-1], nums[pivot_index]

    return quick_sort_left(nums[:pivot_index]) + [nums[pivot_index]] + quick_sort_left(nums[pivot_index + 1 :])


if __name__ == "__main__":
    # array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    # bubble_sort(array)
    # print(array)

    # array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    # selection_sort(array)
    # print(array)

    # array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    # print(insertion_sort(array))

    # array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    # print(merge_sort(array))

    array = [99, 0, 6, 2, 1, 5, 63, 87, 283, 4, 44]
    print(quick_sort_right(array))
    print(quick_sort_left(array))
