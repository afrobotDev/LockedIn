def merge_sort(nums):
    if len(nums) < 2:
        return nums
    mid = len(nums) // 2 # index which divides the list
    first = nums[:mid]   # first half
    second = nums[mid:]  # second half
    # recursively divide each half
    sorted_left_side = merge_sort(first)
    sorted_right_side = merge_sort(second)
    # merge already sorted halves
    return merge(sorted_left_side, sorted_right_side)

def merge(first, second):
    final_list = []
    i = 0
    j = 0
    while i < len(first) and j < len(second):
        if first[i] <= second[j]: 
            final_list.append(first[i]) 
            i += 1
        else:
            final_list.append(second[j])
            j += 1
    
    # Append remaining elements from first list
    while i < len(first):
        final_list.append(first[i])
        i += 1
    
    # Append remaining elements from second list
    while j < len(second):
        final_list.append(second[j])
        j += 1
    
    return final_list

