class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = Counter(nums)
        temp = []
        for i in range (1, len(nums)+1):
            if d[i] == 0:
                temp.append(i)
        return temp

"""
Time Complexity O(n)
Space Complexity O(n)
"""
