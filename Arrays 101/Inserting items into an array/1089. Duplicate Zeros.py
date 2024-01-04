class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        idx = 0
        length = len(arr)
        while idx < length:
            if arr[idx] == 0:
                arr.insert(idx+1, 0)
                idx += 2
            else:
                idx += 1 
        while len(arr) > length:
            arr.pop()

"""
Here we are first inserting the 0 into the array whenever we see a 0.
Then poping out the extra elements from the list.
Time complexity O(n)
Space complexity O(1)
"""
