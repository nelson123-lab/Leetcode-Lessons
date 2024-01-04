class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        k = len(arr)
        i = 0
        while i < k:
            if arr[i] == 0:
                arr.insert(i+1,0)
                i += 2
            else:
                i +=1
        while len(arr) > k:
            arr.pop()
