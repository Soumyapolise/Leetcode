# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        node = slow.next
        
        prev = None
        while node:
            k = node.next
            node.next = prev
            prev = node
            node = k
        
        slow.next = None
        while prev:
            next_node = head.next
            head.next = prev
            # try:
            if prev.next:
                rev_next_node = prev.next
            else:
                rev_next_node = None
            # except:
            #     rev_next_node = None
            prev.next = next_node
            head = next_node
            prev = rev_next_node
            
        