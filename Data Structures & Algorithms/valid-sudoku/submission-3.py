class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            row = [i for i in range(10, 19)]
            row_num = 0
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                else:
                    print(f'row num is {row_num}')
                    row[row_num] = board[i][j]
                    row_num += 1
                if not len(set(row)) == len(row):
                    return False
        
        for i in range(len(board)):
            col = [i for i in range(10, 19)]
            col_num = 0
            for j in range(len(board)):
                if board[j][i] == ".":
                    continue
                else:
                    col[col_num] = board[j][i]
                    col_num += 1
                if not len(set(col)) == len(col):
                    return False

        i_start, i_stop = 0, 3
        j_start, j_stop = 0, 3
        cube = 1

        while j_start < 9:
            square = [i for i in range (10, 19)]
            cube = 0
            for i in range(i_start, i_stop):
                for j in range(j_start, j_stop):
                    if (board[i][j] == "."):
                        continue
                    else:
                        square[cube] = board[i][j]
                    if not len(set(square)) == len(square):
                        return False
                    cube += 1
            if (i_stop == 9):
                j_start += 3
                j_stop += 3
                i_start, i_stop = 0, 3
            else:
                i_start += 3
                i_stop += 3
        
        return True