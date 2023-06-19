class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
#         gain = [0] + gain
        
#         for i in range(1, len(gain)):
#             gain[i] += gain[i-1]
            
#         return max(gain)

        lis=[]
        for i in range(len(gain)):
            lis.append(sum(gain[0:i]))
        lis.append(sum(gain))
        return max(lis)