# Time Complexity: O(n^2)
# Space complexity: O(1)


def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    closestSum = float('inf')
    nums.sort()
    for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            while l<r:
                    currSum = nums[i] + nums[l] + nums[r]
                    if abs(target - currSum) < abs(target - closestSum):
                            closestSum = currSum

                    if currSum < target:
                            l += 1
                    elif currSum > target:
                            r -= 1
                    else:
                        return currSum
    return closestSum


nums = [-1,1,-4,2]
target = 1
res = threeSumClosest(nums,target)
print(res)