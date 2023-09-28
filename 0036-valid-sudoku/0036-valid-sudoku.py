class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        d = {}
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                element = board[i][j]
                if element != ".":
                    if (i, element) in d or (element, j) in d or (element, i//3, j//3) in d:
                        return False
                    d[(i, element)] = 1
                    d[(element, j)] = 1
                    d[(element, i//3, j//3)] = 1
        
        return True
         