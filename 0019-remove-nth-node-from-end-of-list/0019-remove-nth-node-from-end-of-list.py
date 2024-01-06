# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c = 0
        dummy = head
        while dummy:
            c += 1
            dummy = dummy.next
        
        
        k = c - n
        if k == 0:
            return head.next
        c = 0
        
        dummy = head
        while head:
            c += 1
            if c == k:
                if n == 1:
                    node = None
                else:
                    node = head.next.next
                
                head.next.next = None
                head.next = node
                return dummy
        
            head = head.next