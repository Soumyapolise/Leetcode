# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = head
        root = left = ListNode(0)
        right = right_node = ListNode(0)
        while dummy:
            if dummy.val < x:
                left.next = TreeNode(dummy.val)
                left = left.next
            else:
                right.next = TreeNode(dummy.val)
                right = right.next
            dummy = dummy.next
        
        right.next = None
        left.next = right_node.next
        
        return root.next