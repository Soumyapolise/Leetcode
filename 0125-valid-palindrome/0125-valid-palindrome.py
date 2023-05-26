class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        stack = []
        
        for ch in s:
            stack.append(ch)
            if ord(ch)>ord('z') or ord(ch)<ord('a'):
                if not ch.isnumeric():
                    stack.pop()
        
        left, right = 0, len(stack)-1
        while left<right:
            if stack[left] != stack[right]:
                return False
            left += 1
            right -= 1
            
        return True
        