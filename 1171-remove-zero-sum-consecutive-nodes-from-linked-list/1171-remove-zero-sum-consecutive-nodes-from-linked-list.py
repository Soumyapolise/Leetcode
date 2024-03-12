# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        
        while head:
            arr.append(head.val)
            head = head.next
        
        i = 0
        if len(arr) == 1:
            return ListNode(arr[0]) if arr[0] != 0 else None
        while i < len(arr)-1:
            print(i)
            sums = arr[i]
            j = i+1
            while j < len(arr) and sums != 0:
                sums += arr[j]
                j += 1
            
            if sums == 0:
                #print("hi", i ,j)
                arr = arr[0:i] + arr[j:]
                print(arr)
                i = 0
            else:
                i += 1
        
        dummy = head = ListNode(0)
        if len(arr) > 0 and arr[-1] == 0:
            arr = arr[0:-1]
        for x in arr:
            dummy.next = ListNode(x)
            dummy = dummy.next
        
        return head.next