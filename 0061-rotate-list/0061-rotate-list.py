# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head

        # Calculate the length of the linked list
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1

        # Adjust k to be within the length of the list
        k %= length

        # If k is 0, no rotation is needed
        if k == 0:
            return head

        # Find the new head and tail of the rotated list
        current.next = head  # Connect the current tail to the current head
        current = head
        for _ in range(length - k - 1):
            current = current.next
        new_head = current.next
        current.next = None  # Set the new tail's next to None

        return new_head
#         lis = []
#         dummy = head
#         while head:
#             lis.append(head.val)
#             head = head.next
          
#         node = res = ListNode(0)
#         n = len(lis)
#         for i in range(n-k, n):
#             res.next = ListNode(lis[i])
#             res = res.next
        
#         if n > k:
#             j = 0
#             while j < n-k:
#                 res.next = ListNode(dummy.val)
#                 dummy = dummy.next
#                 res = res.next
#                 j += 1
        
#         return node.next