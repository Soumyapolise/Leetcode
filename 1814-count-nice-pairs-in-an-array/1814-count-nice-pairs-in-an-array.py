class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        d = {}
        MOD = 10**9 + 7
        
        for num in nums:
            num = str(num)
            rev_num = num[::-1]
            
            val = int(num) - int(rev_num)
            
            if val in d:
                d[val] = (d[val] + 1) % MOD
            else:
                d[val] = 1
                
        res = 0
        for val in d.values():
            res = (res + math.comb(val, 2)) % MOD
        
        return res
            
        
        