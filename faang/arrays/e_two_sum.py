# [1, 3, 7, 9, 2], t = 11, answer = [3, 4]
# [1, 3, 7, 9, 2], t = 25, answer = None
# [], t = 1, answer = None
# [5], t = 5, answer = None
# [1, 6], t = 7, answer = [0, 1]


# T: O(n**2), S: O(1)
def find_two_sum(nums, target):
    for i in range(len(nums)):
        number_to_find = target - nums[i]
        for j in range(i + 1, len(nums)):
            if nums[j] == number_to_find:
                return [i, j]
    return


# T: O(n), S: O(n)
def find_two_sum_dict(nums, target):
    numbers_to_find = {}
    for i in range(len(nums)):
        if nums[i] in numbers_to_find:
            return [numbers_to_find[nums[i]], i]
        numbers_to_find[target - nums[i]] = i
    return


if __name__ == "__main__":
    inputs = [
        ([1, 3, 7, 9, 2], 11),
        ([1, 3, 7, 9, 2], 25),
        ([], 1),
        ([5], 5),
        ([1, 6], 7),
    ]
    for nums, target in inputs:
        print(find_two_sum(nums, target))
        print(find_two_sum_dict(nums, target))
