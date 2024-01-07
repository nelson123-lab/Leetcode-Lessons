class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        for i in range(len(arr)):
            if arr[i]*2 in (arr[:i] + arr[i +1:]):
                return True
        return False

"""
Here we are checking if the element multiplied by 2 exists in the remaing elements within the array except this one.
Here it automatically satisfies the condition i!= J

Time complexity O(n*2) because there is a search operation happening within in the for loop.
Space Complexity O(1)
"""
        
