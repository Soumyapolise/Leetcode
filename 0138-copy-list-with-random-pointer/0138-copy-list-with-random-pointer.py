"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d = {}
        dummy = node = Node(0)
        dummy2 = head
        while head:
            node.next = Node(head.val)
            d[head] = node.next
            head = head.next
            node = node.next
        
        head = dummy2
        node = dummy.next
        
        while head:
            if head.random:
                node.random = d[head.random]
            else:
                node.random = None
            node = node.next
            head = head.next
        
        return dummy.next