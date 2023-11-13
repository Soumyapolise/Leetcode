class Solution:
    def sortVowels(self, s: str) -> str:
        d = {'a':1, 'e':1, 'o':1, 'u':1, 'i':1, 'A':1, 'E':1, 'O':1, 'I':1, 'U':1}
        
        n = len(s)
        t = ["#" for _ in range(n)]
        arr = []
        
        for i in range(n):
            if s[i] not in d:
                t[i] = s[i]
            else:
                arr.append(s[i])
        
        arr.sort()
        j = 0
        for i in range(n):
            if t[i] == "#":
                t[i] = arr[j]
                j += 1
        
        return "".join(t)
        
        
        