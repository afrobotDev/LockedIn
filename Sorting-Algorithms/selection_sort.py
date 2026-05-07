def selection_sort(nums):
    high = len(nums)
    for i in range(0, high - 1):
        smallest_idx = i
        for j in range(i + 1, high):
            if nums[j] < nums[smallest_idx]:
                smallest_idx = j
        nums[i], nums[smallest_idx] = nums[smallest_idx], nums[i]
    return nums
