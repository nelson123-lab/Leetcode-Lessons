def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

"""
Time Complexity:
Average and Worst Case: 
O(nlogn)
Worst Case: 
O(n2) (rare, depends on pivot selection)
Space Complexity: 
O(logn) (due to recursion stack)
"""
