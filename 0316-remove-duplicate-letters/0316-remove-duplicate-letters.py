class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        d = {}
        
        for i in range(len(s)):
            d[s[i]] = i #storing the last occurrences of every letter in s
            
        stack = []
        seen = set()
        
        for i in range(len(s)):
            if s[i] not in seen:
                while stack and s[i] < stack[-1] and i < d[stack[-1]]: #making sure it is not the last occurrence of the letter
                    seen.remove(stack.pop()) #if the new letter is smaller and not the last occurrence in the string s, remove it from stack, cuz we need the smallest in the lexicographical order
                stack.append(s[i]) #in turn add the smallest here.
                seen.add(s[i])
            
        return "".join(stack)
                    