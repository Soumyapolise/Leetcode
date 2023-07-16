class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        res = []
        
        for num in nums1:
            d[num] = 1
        
        for num in nums2:
            if num in d:
                res.append(num)
        
        return list(set(res))