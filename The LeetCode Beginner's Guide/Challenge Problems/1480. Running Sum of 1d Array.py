class Solution(object):
    def runningSum(self, nums):
        a = nums[0]
        for i in range(1, len(nums)):
            nums[i] = nums[i] + a
            a = nums[i]
        return nums

"""
Time Complexity O(n)
Space Compelxity O(1)

Here we can we avoid the usage of the variable 'a'.
"""

class Solution(object):
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] + nums[i]
            a = nums[i]
        return nums

"""
Time Complexity O(n)
Space Compelxity O(1)
"""
