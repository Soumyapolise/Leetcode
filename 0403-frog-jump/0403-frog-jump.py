class Solution:
    def canCross(self, stones: List[int]) -> bool:
        def dfs(i, k, stones):
            if (k, i) in memo:
                return memo[(k,i)]
            if k == stones[-1]:
                return True
            
            if i-1 > 0 and k + (i-1) in stones:
                if dfs(i-1, k+i-1, stones):
                    memo[(k,i)] = True
                    return True

            if k + i in stones:
                if dfs(i, k+i, stones):
                    memo[(k,i)] = True
                    return True

            if k + i + 1 in stones:
                if dfs(i+1, k+i+1, stones):
                    memo[(k,i)] = True
                    return True
            
            memo[(k,i)] = False
            return False
        
        if stones[1] != 1:
            return False
        
        memo = {}
        return dfs(1, 1, stones)
        