class Solution:
    def countHomogenous(self, s: str) -> int:
        curr_streak = 0
        ans = 0
        MOD = 10**9 + 7
        
        for i in range(len(s)):
            if i == 0 or s[i] == s[i-1]:
                curr_streak += 1
            else:
                curr_streak = 1
            
            ans = (ans + curr_streak) % MOD
        
        return ans % MOD
        
#         d = {}
#         MOD = 10**9 + 7
#         string = "#"
        
#         for i in range(len(s)):
#             if s[i] == string[-1]:
#                 string += s[i]
#                 if string not in d:
#                     d[string] = 1
#                 else:
#                     d[string] += 1
                
#                 for j in range(1, len(string)):
#                     if string[j:] not in d:
#                         d[string[j:]] = 1
#                     else:
#                         d[string[j:]] += 1
#             else:
#                 string = s[i]
#                 if string not in d:
#                     d[string] = 1
#                 else:
#                     d[string] += 1
            
#             d[string] %= MOD
        
# #         print(d)
#         return sum(d.values()) % MOD