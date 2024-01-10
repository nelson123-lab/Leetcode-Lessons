class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        odd, even = [], []
        for v in nums:
            if v % 2 == 0:
                even.append(v)
            else:
                odd.append(v)
        
        return even + odd

"""
Time Complexity O(n)
Space Complexity O(n)
"""

# Solution with in-place operations.
class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] %2 == 0:
                temp = nums[k]
                nums[k] = nums[i]
                nums[i] = temp

                # A simple way to do the same.
                # nums[k], nums[i] = nums[i], nums[k]
                k += 1
            else: pass
        return nums

# We can also do a = a+b , b = a - b, a = a - b
"""
Time Complexity O(n)
Space Complexity O(1)
"""


