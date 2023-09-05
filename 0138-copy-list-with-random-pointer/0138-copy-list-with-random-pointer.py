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
        d = {None:None}
        root = node = ListNode(0)
        head1 = head
        while head:
            node.next = d[head] = ListNode(head.val) #just storing each node (not node's val, but the whole node information in a dictionary, so that later we can access the random pointers)
            head = head.next
            node = node.next
        
        node.next = None
        head = head1
        node = root.next
        
        while head:
            node.random = d[head.random]
            head = head.next
            node = node.next
        
        return root.next
        
        
        