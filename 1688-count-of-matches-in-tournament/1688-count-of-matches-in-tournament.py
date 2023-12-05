class Solution:
    def numberOfMatches(self, n: int) -> int:
#         count = 0
        
#         while n != 1:
#             count += n//2
#             n = math.ceil(n/2)
        
#         return count

##one match eliminates one team, and one team wins, so for the last winner of the game, n-1 teams need to lose, so for n-1 teams to lose - there should be n-1 matches
        return n-1