class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            nums[i] *= nums[i]
        nums.sort()
        return nums
"""
Time Complexity O(n log n) due to sorting. 
Space Complexity O(n) since tim sort takes O(n) space even though the squaring is done in place.
"""
