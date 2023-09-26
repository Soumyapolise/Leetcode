class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
    
        last_occurrence = {char: i for i, char in enumerate(s)}

        seen = set()

        for i, char in enumerate(s):
            if char not in seen:
                while stack and char < stack[-1] and i < last_occurrence[stack[-1]]:
                    seen.discard(stack.pop())
                stack.append(char)
                seen.add(char)

        return ''.join(stack)

# 		for i in range(len(s)):

# 			if s[i] not in visited:
# 				while (stack and stack[-1] > s[i] and last_occ[stack[-1]] > i):
# 					visited.remove(stack.pop())

# 				stack.append(s[i])
# 				visited.add(s[i])

# 		return ''.join(stack)