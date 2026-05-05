def bubble_sort(nums):
    if len(nums) == 0:
        return []
    elif len(nums) == 1:
        return nums
    swapping = True
    end = len(nums)
    while swapping:
        swapping = False
        for i in range(1, end):
            x = nums[i - 1]
            y = nums[i]
            if nums[i - 1] > nums[i]:
                nums[i - 1] = y
                nums[i] = x
                swapping = True
        end -= 1
    return nums
