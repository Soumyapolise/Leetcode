class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for r in range(len(matrix)):
            if target == matrix[r][-1]:
                return True
            elif target < matrix[r][-1]:
                break
        
        i = 0
        j = len(matrix[r]) - 1
        
        while i <= j:
            mid = i + (j-i)//2
            if target == matrix[r][mid]:
                return True
            elif target < matrix[r][mid]:
                j = mid - 1
            else:
                i = mid + 1
        
        return False