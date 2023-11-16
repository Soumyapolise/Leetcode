class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        res = []
        def dfs(ch):
            if len(ch) == n:
                if ch not in nums:
                    res.append(ch)
                    return True
                return False
                
            if dfs(ch + "0"):
                return True
            
            if dfs(ch + "1"):
                return False
        
        dfs("")
        return res[0]
            
            