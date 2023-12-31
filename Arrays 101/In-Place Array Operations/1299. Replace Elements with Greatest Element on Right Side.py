class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        curr_max = arr[-1]
        arr[-1] = -1
        for i in range(len(arr)-2,-1,-1):
            curr = arr[i]
            arr[i] = curr_max
            if curr>curr_max:
                curr_max = curr
        return arr

"""
Here we are first replacing the array's last element with -1 and then considering the array in the reverse order.
The reverse order provides the option not to test for the maximum each time we only need to compare with a single element each time.

Time complexity O(n)
Space Complexity O(1)
"""
