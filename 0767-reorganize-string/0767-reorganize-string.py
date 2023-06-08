class Solution:
    def reorganizeString(self, s: str) -> str:
        d = {}
        res = []
        for ch in s:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1
        
        d = dict(sorted(d.items(), key = lambda x:x[1], reverse=True)) #sorted in decreasing order
        max_count = list(d.values())[0]
        max_char = list(d.keys())[0]
        
        if max_count > (len(s)+1)//2: #getting rid of not possible arrangements
            return ""
              
        for _ in range(max_count):
            res += [max_char] #res = ["a", "a", "a", "a", "a"] if max_char = "a", max_count = 5  
        i = 0
        for key, value in d.items():
            if key == max_char: 
                continue #since we've already added our max_char to res
            for _ in range(value):
                res[i] += key #just adding different chars next to our previous values in res. #Pigeonhole principle
                if i != len(res)-1:
                    i+=1
                else:
                    i=0
                    
        return "".join(res)