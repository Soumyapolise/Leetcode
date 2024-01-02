class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.p = []
        sums = sum(self.w)
        for n in self.w:
            self.p.append(n/sums)
            
    def pickIndex(self) -> int:
        w = self.w
        p = self.p
        
        return random.choices(range(len(w)), weights = tuple(p))[0]

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()