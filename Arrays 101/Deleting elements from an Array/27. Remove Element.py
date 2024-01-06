class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

"""
Here every element is getting inserted into the first postion if it is not a val so that the first k values will be retured.
Time Compelxity O(n)
Space Complexity O(1)
"""
