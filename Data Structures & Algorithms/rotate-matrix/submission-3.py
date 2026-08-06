class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        total = n - 1
        for layer in range(n // 2):
            for offset in range(layer, total - layer):
                tl = (layer, offset)
                tr = (offset, total - layer)
                br = (total - layer, total - offset)
                bl = (total - offset, layer)
                temp = matrix[tl[0]][tl[1]]
                matrix[layer][offset] = matrix[bl[0]][bl[1]]
                matrix[total - offset][layer] = matrix[br[0]][br[1]]
                matrix[total - layer][total - offset] = matrix[tr[0]][tr[1]]
                matrix[offset][total - layer] = temp


