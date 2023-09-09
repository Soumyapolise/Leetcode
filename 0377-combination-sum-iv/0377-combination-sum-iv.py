class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        d = {}
        d[0] = 1
        
        def search(target):
            if target in d:
                return d[target]
            
            comb_sum = 0
            
            for num in nums:
                if target > num:
                    comb_sum += search(target-num)
                elif target == num:
                    comb_sum += 1
            
            d[target] = comb_sum
            return d[target]
        
        return search(target)
            