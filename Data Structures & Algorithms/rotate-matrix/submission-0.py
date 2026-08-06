class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for layer in range(n // 2):
            first, last = layer, n - 1 - layer

            for i in range(first, last):
                offset = i - first

                top_left     = (first, i)
                top_right    = (i, last)
                bottom_right = (last, last - offset)
                bottom_left  = (last - offset, first)

                # save top_left, then overwrite in rotational order,
                # then drop the saved value into top_right's spot
                temp = matrix[top_left[0]][top_left[1]]
                matrix[top_left[0]][top_left[1]] = matrix[bottom_left[0]][bottom_left[1]]
                matrix[bottom_left[0]][bottom_left[1]] = matrix[bottom_right[0]][bottom_right[1]]
                matrix[bottom_right[0]][bottom_right[1]] = matrix[top_right[0]][top_right[1]]
                matrix[top_right[0]][top_right[1]] = temp