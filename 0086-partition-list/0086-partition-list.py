# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        stack = []
        dummy = head
        left = []
        right = []
        while dummy:
            if dummy.val < x:
                left.append(dummy.val)
            else:
                right.append(dummy.val)
            dummy = dummy.next
                
        dummy = root = TreeNode(0)
        for n in left:
            dummy.next = TreeNode(n)
            dummy = dummy.next
        
        for n in right:
            dummy.next = TreeNode(n)
            dummy = dummy.next
        
        dummy.next = None
        
        return root.next