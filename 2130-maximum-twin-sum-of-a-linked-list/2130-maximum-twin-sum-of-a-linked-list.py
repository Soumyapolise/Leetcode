# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        res = []
        n, i = 0, 0
        dummy = head
        while dummy:
            n+=1
            dummy = dummy.next
        
        dummy = head
        while i<n//2:
            res.append(dummy.val)
            i+=1
            dummy = dummy.next
        i = 1
        while dummy:
            res[-i] += dummy.val
            dummy = dummy.next
            i+=1
        
        return max(res)
            