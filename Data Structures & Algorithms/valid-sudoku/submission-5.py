class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = 0
        for i in range(9):
            row = [i for i in range(10, 19)]
            r = 0
            for j in range(9):
                if board[i][j] == ".":
                    continue
                else:
                    row[r] = board[i][j]
                    r += 1
                if not len(set(row)) == len(row):
                    return False
        
        c = 0
        for i in range(9):
            col = [i for i in range(10, 19)]
            c = 0
            for j in range(9):
                if board[j][i] == ".":
                    continue
                else:
                    col[c] = board[j][i]
                    c += 1
                if not len(set(col)) == len(col):
                    print(f'{set(col)}, {col}')
                    return False
        
        i_start, i_stop = 0, 3
        j_start, j_stop = 0, 3

        while j_start < len(board):
            square = [x for x in range(10, 19)]
            for i in range(i_start, i_stop):
                for j in range(j_start, j_stop):
                    print(i, j)
                    if board[i][j] == ".":
                        continue
                    square.append(board[i][j])
                    if not len(set(square)) == len(square):
                        print('square')
                        return False
            if i_stop == len(board):
                i_start, i_stop = 0, 3
                j_start += 3
                j_stop += 3
            else:
                i_start += 3
                i_stop += 3
        return True

                    
