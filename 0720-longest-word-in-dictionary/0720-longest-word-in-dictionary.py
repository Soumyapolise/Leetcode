class Solution:
    def longestWord(self, words: List[str]) -> str:
        valid = set([""])
       
        for word in sorted(words, key=lambda x: len(x)):
            if word[:-1] in valid:
                valid.add(word)
		
        return max(sorted(valid), key=lambda x: len(x))
            
        
#         words.sort(reverse = True)
#         print(words)
#         left = 0
#         j = -1
#         res = ""
#         maxL = float('-inf')
#         for i in range(1, len(words)):
#             if words[i] + words[left][j:] == words[left]:
#                 j -= 1
#                 l = len(words[left])
#                 if j == -1*(l):
#                     if l >= maxL:
#                         res = words[left]
#                         maxL  = l
#                     left = i + 1
#                     j = -1
#             else:
#                 left = i
#                 j = -1
        
#         return res