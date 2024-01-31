# [5, 3, 1, 6, 4, 2], k = 2 ===> [1, 2, 3, 4, 5, 6], answer = 5
# [2, 3, 1, 2, 4, 2], k = 4 ===> [1, 2, 2, 2, 3, 4], answer = 2
# [3], k = 1 ===> [3], answer = 3


# T: O(n**2), Θ(n), S: O(1) - with tail recursion, O(n**2) - without
def kth_largest_element(nums, k):
    if len(nums) <= 1:
        return nums[-k]

    index, pivot_index = 0, 0
    while index < len(nums):
        if nums[index] < nums[-1]:
            nums[pivot_index], nums[index] = nums[index], nums[pivot_index]
            pivot_index += 1
        index += 1
    nums[pivot_index], nums[-1] = nums[-1], nums[pivot_index]

    if len(nums) - pivot_index == k:
        return nums[pivot_index]
    elif len(nums) - pivot_index < k:
        return kth_largest_element(nums[:pivot_index], k - len(nums[pivot_index:]))
    else:
        return kth_largest_element(nums[pivot_index + 1 :], k)


def partition(array, left, right):
    pivot_element = array[right]
    partition_index = left
    for j in range(left, right):
        if array[j] < pivot_element:
            array[partition_index], array[j] = array[j], array[partition_index]
            partition_index += 1
    array[partition_index], array[right] = array[right], array[partition_index]
    return partition_index


def quick_sort(array, left, right):
    if left < right:
        partition_index = partition(array, left, right)
        quick_sort(array, left, partition_index - 1)
        quick_sort(array, partition_index + 1, right)


# T: O(n**2), Θ(nlogn), S: O(logn)
def get_kth_largest_quick_search(array, k):
    index_to_find = len(array) - k
    quick_sort(array, 0, len(array) - 1)
    return array[index_to_find]


def quick_select(array, left, right, index_to_find):
    if left < right:
        partition_index = partition(array, left, right)
        if index_to_find == partition_index:
            return array[partition_index]
        elif index_to_find < partition_index:
            return quick_select(array, left, partition_index - 1, index_to_find)
        else:
            return quick_select(array, partition_index + 1, right, index_to_find)
    elif left == right:
        return array[left]


# T: O(n**2), Θ(n), S: O(1) - with tail recursion, O(n)? - without
def get_kth_largest_quick_select(array, k):
    index_to_find = len(array) - k
    return quick_select(array, 0, len(array) - 1, index_to_find)


if __name__ == "__main__":
    inputs = [
        ([5, 3, 1, 6, 4, 2], 2),
        ([2, 3, 1, 6, 4, 5], 2),
        ([2, 3, 1, 2, 4, 2], 4),
        ([3], 1),
        ([3, 2, 1, 5, 6, 4], 2),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4),
        ([2, 1], 1),
    ]
    for array, k in inputs:
        # print(kth_largest_element(array, k))
        # print(get_kth_largest_quick_search(array, k))
        print(get_kth_largest_quick_select(array, k))
