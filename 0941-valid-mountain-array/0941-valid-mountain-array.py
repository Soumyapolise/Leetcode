class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i, j, n = 0, len(arr) - 1, len(arr)
        
        while i < n-1 and arr[i] < arr[i + 1]: 
            i += 1
            
        while j > 0 and arr[j - 1] > arr[j]: 
            j -= 1
            
        return 0 < i == j < n - 1