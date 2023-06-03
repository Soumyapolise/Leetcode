class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {}
        left = 0
        maxi = 0
        for right in range(len(fruits)):
            if fruits[right] in basket:
                basket[fruits[right]] += 1
            else:
                basket[fruits[right]] = 1
            
            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    basket.pop(fruits[left])
                left += 1
            
            maxi = max(maxi, right-left+1)
        
        return maxi