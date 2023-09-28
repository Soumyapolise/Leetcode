# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         d = {}
        
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 element = board[i][j]
#                 if element != ".":
#                     if (i, element) in d or (element, j) in d or (element, i//3, j//3) in d:
#                         return False
#                     d[(i, element)] = 1
#                     d[(element, j)] = 1
#                     d[(element, i//3, j//3)] = 1
        
#         return True
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != ".":
                    # Check the row, column, and box constraints
                    if element in rows[i] or element in cols[j] or element in boxes[i // 3 * 3 + j // 3]:
                        return False
                    rows[i].add(element)
                    cols[j].add(element)
                    boxes[i // 3 * 3 + j // 3].add(element)

        return True

         