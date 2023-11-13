# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        
        while head:
            dummy = head.next
            head.next = prev
            prev = head
            head = dummy
        
        reverse = prev
        carry = 0
        while prev:
            val = prev.val * 2 + carry
            prev.val = val % 10
            carry = val // 10
            if prev.next:
                prev = prev.next
            else:
                break
        
        if carry != 0:
            prev.next = ListNode(carry)
            prev = prev.next
        
        prev = None
        while reverse:
            dummy = reverse.next
            reverse.next = prev
            prev = reverse
            reverse = dummy
        
        return prev
            