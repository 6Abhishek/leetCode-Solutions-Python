# Time Complexity: O(n^2)
# Space Complexity: O(1)

def twoSum(nums: list[int], target: int):
    l = len(nums)

    for i in range(l):
        for j in range(i+1):
            if nums[i] + nums[j] == target:
                return [j,i]   # first element is 'i' and second one is 'j'
    return []       
print(twoSum([2,7,11,15],9))