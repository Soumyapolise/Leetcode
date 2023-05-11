class Solution:
    def exist(self, matrix: List[List[str]], word: str) -> bool:
        d = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] in d:
                    d[matrix[i][j]] += 1
                else:
                    d[matrix[i][j]] = 1
        print(d)
        for k in range(len(word)):
            if word[k] not in d or word.count(word[k])>d[word[k]]:
                return False
        
        k = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == word[0]:
                    board = matrix
                    if self.dfs(board, i, j, word, 0):
                        return True
    
        return False
    
    def dfs(self, board, i, j, word, k):
            if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or k>=len(word) or word[k] != board[i][j]:
                return False
            
            if k == len(word)-1:
                return True

            directions = [(-1,0), (1,0), (0,1), (0,-1)]

            for x, y in directions:
                tmp = board[i][j]
                board[i][j] = -1
                
                if self.dfs(board, i+x, j+y, word, k+1):
                    return True
                board[i][j] = tmp #restoring the original value of board[i][j]
            

                
            
            
            
            