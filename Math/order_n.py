def find_max(nums):
        maximum = float('-inf')
        for num in nums:
            if num > maximum:
                maximum = num
        return maximum 
