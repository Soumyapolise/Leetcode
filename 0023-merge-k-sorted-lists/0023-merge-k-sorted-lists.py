# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        mid = len(lists)//2
        l = self.mergeKLists(lists[0:mid:])
        r = self.mergeKLists(lists[mid::])
        return self.mergeList(l, r)
            
        
    def mergeList(self, l:ListNode, r:ListNode):
        dummy = ListNode(0)
        head = dummy
        while l and r:
            if l.val<r.val:
                dummy.next = l
                l = l.next
            else:
                dummy.next = r
                r = r.next
            dummy = dummy.next
        if l:
            dummy.next = l
        if r:
            dummy.next = r
        return head.next
        
    
    
    
    ####### O(nlogn)
        # lis = []
        # for l in lists:
        #     while l:
        #         lis.append(l.val)
        #         l = l.next
        # lis.sort()
        # root = ListNode(0)
        # head = root
        # for x in lis:
        #     root.next = ListNode(x)
        #     root = root.next
        #     # root = root.next
        # return head.next
        
        