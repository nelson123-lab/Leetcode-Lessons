class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        for i in range(1, len(nums)):
            if nums[k] != nums[i]:
                k += 1
                nums[k] = nums[i]
            else: pass
        return k + 1

"""
Replacing the duplicate values inplace to keep only the non-duplicate values infront.
Here the k += 1 is placed below the replacing because only when there is a change the replacing should happen and it should happen in the place of duplicate elements
not on unique elements. So we need to increase the index whenever there is a change.

Time Complexity O(n)
Space Complexity O(1)
"""
