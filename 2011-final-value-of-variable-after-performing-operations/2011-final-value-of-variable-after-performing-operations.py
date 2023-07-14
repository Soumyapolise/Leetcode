class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        d = {"--X":-1, "X--":-1, "X++":1, "++X":1}
        
        res = 0
        for ch in operations:
            res += d[ch]
        
        return res