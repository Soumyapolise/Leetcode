# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], p: int) -> List[Optional[ListNode]]:
        n = 0
        dummy = head
        while head:
            n += 1
            head = head.next #counting the length
        
        rem = n % p
        k = n//p
        res = []
        i = 0
        if n <= p:
            while dummy:
                res.append(ListNode(dummy.val))
                dummy = dummy.next
            
            l = len(res)
            while l < p:
                res.append(ListNode(None).next) #adding empty lists
                l += 1
            return res
        
        while dummy:
            if i == 0:
                node = ListNode(dummy.val) #new list start
                res.append(node)
                i += 1
            elif i < k:
                node.next = ListNode(dummy.val)
                node = node.next
                i += 1
                
            dummy = dummy.next
            
            if i == k:
                if rem > 0:
                    node.next = ListNode(dummy.val)
                    node = node.next
                    node.next = None
                    rem -= 1
                    dummy = dummy.next
                i = 0
        
        return res