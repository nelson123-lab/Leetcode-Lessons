class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        cons_max = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
                cons_max = max(count, cons_max)
            else:
                count = 0
        return cons_max

"""
TIme Complexity O(n)
Space Complexity O(1)
"""
