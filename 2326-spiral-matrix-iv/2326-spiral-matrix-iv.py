# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1 for _ in range(n)] for _ in range(m)]
        
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        
        top, bottom, left, right = 0, m-1, 0, n-1
        direction = 0 #0 = right, 1 = down, 2 = left, 3 = up
        
        index = 0
        while top <= bottom and left <= right:
            if direction == 0:
                for i in range(left, right+1):
                    if index < len(arr):
                        res[top][i] = arr[index]
                    index += 1
                top += 1
            if direction == 1:
                for i in range(top, bottom+1):
                    if index < len(arr):
                        res[i][right] = arr[index]
                    index += 1
                right -= 1
            if direction == 2:
                for i in range(right, left-1, -1):
                    if index < len(arr):
                        res[bottom][i] = arr[index]
                    index += 1
                bottom -= 1
            if direction == 3:
                for i in range(bottom, top-1, -1):
                    if index < len(arr):
                        res[i][left] = arr[index]
                    index += 1
                left += 1
            direction = (direction+1)%4
        
        return res
        
                