class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = len(ratings)
        
        res = [1 for _ in range(candies)]
        
        for i in range(candies):
            if i > 0 and ratings[i] > ratings[i-1]:
                if res[i] <= res[i-1]:
                    res[i] = res[i-1] + 1
                    
        for i in range(candies - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and res[i] <= res[i + 1]:
                res[i] = res[i + 1] + 1
                    
        return sum(res)
        