class Solution:
    def minOperations(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 0
            d[n] += 1
        
        count = 0
        
        for key, val in d.items():
            while val > 0:
                if val == 1:
                    return -1
                elif val == 2 or val == 4:
                    count += val//2
                    val = 0
                else:
                    count += 1
                    val -= 3
        
        return count