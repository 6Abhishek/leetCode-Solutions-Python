# Time Complexity: O(n)
# Space Complexity: O(n)

def twoSum(nums,target):
    nums_map ={}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in nums_map:
            return [nums_map[complement],i]
        nums_map[num] = i
    return []

nums = [3,3] 
target = 6
print(twoSum(nums,target))