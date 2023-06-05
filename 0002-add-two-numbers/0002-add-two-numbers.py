# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lis1 = []
        lis2 = []
        while l1:
            lis1.append(str(l1.val))
            l1 = l1.next
        
        while l2:
            lis2.append(str(l2.val))
            l2 = l2.next
        
        num1 = int("".join(lis1[::-1]))
        num2 = int("".join(lis2[::-1]))
        num = num1 + num2
        lis1 = [ch for ch in str(num)]
        lis1 = lis1[::-1]
        res = dummy = ListNode(0)
        for ch in lis1:
            dummy.next = ListNode(int(ch))
            dummy = dummy.next
        
        dummy.next = None
        
        return res.next
            