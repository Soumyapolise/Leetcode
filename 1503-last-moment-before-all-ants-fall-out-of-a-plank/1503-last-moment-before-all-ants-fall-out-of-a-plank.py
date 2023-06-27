class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        if left == []:
            return n - min(right)
        
        if right == []:
            return max(left)
        
        return max(max(left), n-min(right))
#         count = 0 
        
#         while left != [] and right != []:
#             d = {}
#             i = 0
#             while i < len(left):
#                 left[i] -= 1
#                 if left[i] < 0:
#                     left = left[0:i] + left[i+1:]
#                 else:
#                     i += 1
#             j = 0
#             while j < len(right):
#                 right[j] += 1
#                 if right[j] > n:
#                     right = right[0:j] + right[j+1:]
#                 else:
#                     j += 1
            
#             count += 1
#         # print(left, right)
#         if left == [] and right == []:
#             return count-1
#         elif left == []:
#             return count + n - min(right)
#         else:
#             return count + max(left)
        
        