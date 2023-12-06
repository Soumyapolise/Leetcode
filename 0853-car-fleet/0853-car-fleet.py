class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = [(p, s) for p, s in zip(position, speed)]
        
        pairs.sort(reverse = True)
        
        for p, s in pairs:
            if not stack:
                stack.append((target - p) / s)
            else:
                if (target - p) / s > stack[-1]:
                    stack.append((target - p) / s)
        
        return len(stack)
        
        