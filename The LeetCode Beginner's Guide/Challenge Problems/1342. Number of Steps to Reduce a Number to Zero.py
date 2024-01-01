class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        while num != 0:
            if num % 2 == 0:
                num = num/2
                count += 1
            else:
                num = num - 1
                count += 1
        return count

"""
Time Complexity O(log n)
Space Complexity O(1)
"""

"""
We can further reduce the memory usage by using a recursive approach.
"""
class Solution(object):
    def numberOfSteps(self, num):
        if num == 0:
            return 0
        return 1 + self.numberOfSteps(num - 1 if num & 1 else num >> 1)
"""
Time Complexity O(logn)
Space Complexity O(logn)
"""
