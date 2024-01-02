class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                count += 1
            else: pass
        return count

"""
Time Complexity O(n)
Space Complexity O(1)
"""

# One-liner
class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(map(lambda x: len(str(x))%2 == 0, nums))

"""
Here time and space complexity remains the same as above but an optimal solution. If we are using list comprehension instead of map function our space complexity becomes O(n) as well.
"""
