class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        richest = 0
        for i in accounts:
            if sum(i) > richest:
                richest = sum(i)
        return richest
"""
Here we are taking the sum of each of the customer and check if it is the largest amount each time.

Time Complexity O(n*m) where n is the customers and m represents the bank account of each customer.
Space Complexity O(1)
"""

# One-liner solution using the map function.
class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        return max(map(sum, accounts))
"""
Time and space complexities are same.
"""
