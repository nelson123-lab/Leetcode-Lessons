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
