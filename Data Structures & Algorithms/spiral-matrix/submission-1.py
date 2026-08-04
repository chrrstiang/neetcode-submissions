class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i, j = 0, 0
        i_start, i_stop = 0, len(matrix[0])
        j_start, j_stop = 0, len(matrix)
        total = len(matrix) * len(matrix[0])
        mat = []
        while not len(mat) == total:
            while i < i_stop:
                mat.append(matrix[j][i])
                i += 1
            i -= 1
            j += 1
            i_stop -= 1
            if (len(mat) == total):
                return mat
            while j < j_stop:
                mat.append(matrix[j][i])
                j += 1
            j -= 1
            i -= 1
            j_stop -= 1
            if (len(mat) == total):
                return mat
            while i >= i_start:
                mat.append(matrix[j][i])
                i -= 1
            i += 1
            j -= 1
            i_start += 1
            if (len(mat) == total):
                return mat
            while j >= j_start + 1:
                mat.append(matrix[j][i])
                j -= 1
            j += 1
            i += 1
            j_start += 1
            if (len(mat) == total):
                return mat
        return mat
