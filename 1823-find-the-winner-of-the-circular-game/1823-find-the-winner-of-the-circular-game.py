class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i+1 for i in range(n)]
        
        i = 0
        while len(arr) > 1:
            n = len(arr) #5
            idx = (i + k - 1) % n
            arr = arr[0:idx] + arr[idx+1:]
            i = idx
        
        return arr[0]
            