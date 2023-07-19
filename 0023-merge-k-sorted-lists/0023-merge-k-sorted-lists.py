# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lis = []
        
        for l in lists:
            while l:
                lis.append(l.val)
                l = l.next
        
        lis = sorted(lis)
        
        dummy = root = ListNode(0)
        for x in lis:
            root.next = ListNode(x)
            root = root.next
        
        root.next = None
        
        return dummy.next