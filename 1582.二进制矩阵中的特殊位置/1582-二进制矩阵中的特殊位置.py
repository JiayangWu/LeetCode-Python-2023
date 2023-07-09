class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = set()
        cols = set()
        for i, row in enumerate(mat):
            if sum(row) == 1:
                rows.add(i)

        for j, col in enumerate(zip(*mat)):
            if sum(col) == 1:
                cols.add(j)
        res = 0
        for i in rows:
            for j in cols:
                if mat[i][j] == 1:
                    res += 1
        return res
        # return min(rows_count, cols_count)