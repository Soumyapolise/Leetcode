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
            return lists[-1]
        
        mid = len(lists)//2
        l = self.mergeKLists(lists[0:mid])
        r = self.mergeKLists(lists[mid:])
        return self.mergeList(l, r)
    
    def mergeList(self, l, r):
        dummy = node = ListNode(0)
        while l and r:
            if l.val < r.val:
                node.next = ListNode(l.val)
                l = l.next
            else:
                node.next = ListNode(r.val)
                r = r.next
            node = node.next
        
        if l:
            node.next = l
        
        if r:
            node.next = r
        
        return dummy.next
        
    
    
    
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
        
        