class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        d = {}
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    if (i, board[i][j]) in d or (board[i][j], j) in d or (i//3, j//3, board[i][j]) in d:
                        return False
                    
                    d[(i, board[i][j])] = 1
                    d[(board[i][j], j)] = 1
                    d[(i//3, j//3, board[i][j])] = 1
        
        return True


         