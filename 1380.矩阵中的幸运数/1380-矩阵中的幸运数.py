class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row_index2min = dict()
        col_index2max = dict()

        for i, row in enumerate(matrix):
            row_index2min[i] = min(row)

        for j, col in enumerate(zip(*matrix)):
            col_index2max[j] = max(col)

        res = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == row_index2min[i] == col_index2max[j]:
                    res.append(matrix[i][j])
        return res