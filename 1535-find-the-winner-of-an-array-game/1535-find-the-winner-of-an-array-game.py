class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        
        score = 0
        
        curr = arr[0]
        for i in range(1, n):
            if arr[i] < curr:
                score += 1
            else:
                if score >= k:
                    return curr
                curr = arr[i]
                score = 1
        
        return curr