class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        
        def valid(k):
            if len1%k != 0 or len2%k != 0:
                return False
            
            n1 = len1//k
            n2 = len2//k
            base = str1[:k]
            return str1 == base * n1 and str2 == base * n2
        
        for i in range(min(len1, len2), 0, -1):
            if valid(i):
                return str1[:i]
        
        return ""