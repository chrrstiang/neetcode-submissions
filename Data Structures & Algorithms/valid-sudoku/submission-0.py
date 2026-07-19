class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = set()
        col = set()
        box = [set() for _ in range(9)]
        for i, b in enumerate(board):
            row.clear()
            col.clear()
            for j in range(len(b)):
                if board[i][j] not in row:
                    if board[i][j] != ".":
                        row.add(board[i][j])
                else:
                    return False
                if board[j][i] not in col:
                    if board[j][i] != ".":
                        col.add(board[j][i])
                else:
                    return False
                if board[i][j] not in box[(i // 3) * 3 + (j // 3)]:
                    if board[i][j] != ".":
                        box[(i // 3) * 3 + (j // 3)].add(board[i][j])
                else:
                    return False
        return True