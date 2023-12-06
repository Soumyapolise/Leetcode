class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = [(p, s) for p, s in zip(position, speed)]
        
        pairs.sort(reverse = True)
        
        ##basically, we are going through the pairs in reverse sorted order, and figuring out for the current car and the last seen car(that is in stack), if the current car reaches the target before or at the same time as the car at stack[-1] - if it does, that means they are going to meet at some time before the target, and since the stack[-1] car is slower, that will remain in the stack (making a fleet), and we continue the process of checking the other cars. At last, the number of fleets remaining in stack is the answer!
        for p, s in pairs:
            if not stack:
                stack.append((target - p) / s)
            else:
                if (target - p) / s > stack[-1]:
                    stack.append((target - p) / s)
        
        return len(stack)
        
        