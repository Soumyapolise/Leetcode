class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        
        n = len(arr)
        q = n//20
        
        return sum(arr[q:n-q])/(n-q-q)