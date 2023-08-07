class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][-1] == target:
                return True
            elif matrix[i][-1] > target:
                # print("hi")
                l = 0
                r = len(matrix[0])-1
                while l <= r:
                    mid = l + (r-l)//2
                    if matrix[i][mid] == target:
                        return True
                    if matrix[i][mid] > target:
                        r = mid-1
                    else:
                        l = mid+1
                return False
            
        return False