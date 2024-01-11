class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        ord_height = sorted(heights)
        k = 0
        for i in range(len(heights)):
            if heights[i] != ord_height[i]:
                k += 1
            else: pass
        return k

"""
Time Complexity O(n)
Space Complexity O(n) due to the usage of extra array.
"""
