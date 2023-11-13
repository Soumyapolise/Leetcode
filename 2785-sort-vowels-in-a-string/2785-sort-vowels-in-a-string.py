class Solution:
    def sortVowels(self, s: str) -> str:
        d = {'A':0, 'E':0, 'I':0, 'O':0, 'U':0, 'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
        
        n = len(s)
        t = ["#" for _ in range(n)]
        
        for i in range(n):
            if s[i] not in d:
                t[i] = s[i]
            else:
                d[s[i]] += 1
        
        for i in range(n):
            if t[i] == "#":
                for key, val in d.items():
                    if val != 0:
                        t[i] = key
                        d[key] -= 1
                        break
        
        return "".join(t)
        
        
        