class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = len(arr)//4
        
        d = {}
        
        for num in arr:
            if num not in d:
                d[num] = 0
            d[num] += 1
            
            if d[num] > count:
                return num
        