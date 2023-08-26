class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
    # Sort pairs based on their ending values
        pairs.sort(key=lambda x: x[1])

        # Initialize variables to keep track of the current end value and the chain length
        current_end = float('-inf')  # Initialize to negative infinity
        max_length = 0

        for pair in pairs:
            if pair[0] > current_end:
                # If the current pair can be added to the chain, update the current end value
                current_end = pair[1]
                max_length += 1

        return max_length

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
                