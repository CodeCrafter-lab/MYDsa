def two_sum(nums, target):
    num_map = {}  # stores num: index

    for index, num in enumerate(nums):
        diff = target - num
        if diff in num_map:
            return [num_map[diff], index]
        num_map[num] = index

    return []  # if no solution is found
