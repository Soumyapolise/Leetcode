class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        min_val, max_val = min(arr), max(arr)
        n = len(arr)
        
        if max_val == min_val:
            return True
        
        if (max_val-min_val)%(n-1) != 0:
            return False
        
        diff = (max_val-min_val)//(n-1)
        
        nums = set()
        
        for a in arr:
            if (a-min_val)%(diff)%(n-1) != 0:
                return False
            nums.add(a)
        
        return len(nums) == n