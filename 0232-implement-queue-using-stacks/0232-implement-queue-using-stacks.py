class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
#         if stack1:
#             for y in stack1:
#                 stack2.append(y)
        
        self.stack1.append(x)

    def pop(self) -> int:
        stack1 = self.stack1
        stack2 = self.stack2
        
        while stack1:
            stack2.append(stack1.pop())
        
        val = stack2.pop()
        
        while stack2:
            stack1.append(stack2.pop())
        return val

    def peek(self) -> int:
        return self.stack1[0]

    def empty(self) -> bool:
        return self.stack1 == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()