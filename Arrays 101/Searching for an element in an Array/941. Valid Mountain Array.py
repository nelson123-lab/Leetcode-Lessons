class Solution(object):
    def validMountainArray(self, arr):

      # Minimum 3 elements is required for a valid mountain
      if len(arr) < 3:
          return False

      # Finding the peak index to split the mountain into left and right
      peak_index = arr.index(max(arr))
      left, right = arr[:peak_index + 1], arr[peak_index:]

      # If any of left or right just exist with the peak it is not a valid mountain.
      if len(left) == 1 or len(right) == 1:
          return False

      # Checking if the slope of left is strict.
      for i in range(len(left)):
          if i == len(left)-1: break
          elif left[i] < left[i+1]: pass
          else: return False

      # Checking if the slope of right is strict.
      for i in range(len(right)):
          if i == len(right)-1: break
          elif right[i] > right[i+1]: pass
          else: return False

      return True

"""
Approach:
- Finding the peak of the mountain is the first step so that we can consider the left and right part of the mountain separately.
Time Complexity O(n)
Space Complexity O(n) due to left and right array.
"""
