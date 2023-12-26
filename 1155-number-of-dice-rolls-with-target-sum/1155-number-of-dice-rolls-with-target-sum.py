class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10**9 + 7
        m = [[0] * (target + 1) for i in range(n+1)]

        for i in range(1,k + 1):
            if i > target:
                break
            m[1][i] = 1
        
            
        for row in range(2, n + 1):# use curS like a sliding window
            curS = 0
            for col in range (row, row * k + 1):
                if col >= len(m[0]): #col out of range
                    break
                elif col <= k: # window is not full in these range (0~k-1)
                    curS += m[row-1][col-1]
                    m[row][col] = curS % mod
                else: # when index > k and the sliding window is full, then do the sliding window process
                    curS = curS + m[row-1][col-1] - m[row-1][col-1-k]
                    m[row][col] = curS % mod
                    
                if m[row][col] == 0:
                    break
        
        
        return m[n][target]
        