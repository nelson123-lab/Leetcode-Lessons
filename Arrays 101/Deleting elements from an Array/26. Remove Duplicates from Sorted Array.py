class Solution(object):
    def removeDuplicates(self, nums):
        k = 0
        for i in range(1, len(nums)):
            if nums[k] != nums[i]:
                k += 1
                nums[k] = nums[i]
        return k + 1
"""
Here k value is increased whenever there is new element appears so that the slow pointer that is the k updates non duplicate values.
TIme Complexity O(n)
Space Complexity O(1)
"""
