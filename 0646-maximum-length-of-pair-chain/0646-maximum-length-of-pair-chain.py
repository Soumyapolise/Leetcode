class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x:x[1])
        
        res = 0
        curr_end = float('-inf')
        
        ######GREEDY APPROACH ######, just taking in the first interval that you find that has smaller end point, thereby increasing range of intervals you can take in, there by increasing the "chain" as being asked by the question, to return the longest chain:
        
        for p in pairs:
            if p[0] > curr_end:
                curr_end = p[1]
                res += 1
        
        return res
        
        
    #DFS APPROACH - TLE
#     def findLongestChain(self, pairs: List[List[int]]) -> int:
#         pairs = sorted(pairs)
        
#         res = []
#         for i in range(len(pairs)):
#             self.connect(pairs[i], 1, pairs[i+1:], res)
        
#         return max(res)
    
#     def connect(self, p, l, pairs, res):
#         res.append(l)
#         if pairs == []:
#             return
        
#         for i in range(len(pairs)):
#             if p[1] < pairs[i][0]:
#                 self.connect(pairs[i], l+1, pairs[i+1:], res)
                