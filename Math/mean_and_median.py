def average_followers(nums):
    if len(nums) == 0:
        return None
    total= 0
    for i in nums:
        total += i
    return total/ len(nums)




