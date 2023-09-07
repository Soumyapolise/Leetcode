# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        lis = []
        if left == right:
            return head
        
        while head:
            lis.append(head.val)
            head = head.next
        
        dummy = res = ListNode(0)
        i = 0
        while i < left-1:
            res.next = ListNode(lis[i])
            res = res.next
            i += 1
        
        j = right-1
        while j > left - 2:
            res.next = ListNode(lis[j])
            res = res.next
            j -= 1
        
        k = right
        while k < len(lis):
            res.next = ListNode(lis[k])
            res = res.next
            k += 1
        
        return dummy.next