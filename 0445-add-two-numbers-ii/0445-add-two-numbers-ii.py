# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        while l1:
            num1 = num1*10 + l1.val
            l1 = l1.next
        
        num2 = 0
        while l2:
            num2 = num2*10 + l2.val
            l2 = l2.next
        
        num1 += num2
        
        dummy = root = ListNode(0)
        for n in str(num1):
            root.next = ListNode(int(n))
            root = root.next
        
        return dummy.next