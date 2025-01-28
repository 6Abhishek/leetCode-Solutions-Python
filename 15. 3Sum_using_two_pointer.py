# Time Complexity: O(n^2)
# Space Complexity: O(1)

def threeSum(nums):
    three_sum_list = []
    nums.sort()
    for i, num in enumerate(nums):
        if i > 0 and num == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l < r:
            three_sum = num + nums[l] + nums[r]
            if three_sum > 0:
                r -= 1
            elif three_sum < 0:
                l += 1
            else:
                three_sum_list.append([num, nums[l], nums[r]])
                l += 1
                while ((nums[l] == nums[l-1]) and l < r):
                    l += 1
                    
    return three_sum_list

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))

