class Solution:
    def countVowelPermutation(self, n: int) -> int:
        if n == 0:
            return 0
        
        a = e = i = o = u = 1
        
        for _ in range(n-1): ##we are calculating all the strings of length n, starting from each vowel according to the set conditions
            a, e, i, o, u = e, a + i, a + e + o + u, i + u, a
        
        return (a + e + i + o + u) % (10**9 + 7) ##now that we have the number of strings starting with each vowel, let's just add all the number of strings together and return it.
    