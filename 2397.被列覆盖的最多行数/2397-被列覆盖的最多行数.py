class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        m, n = len(matrix), len(matrix[0])

        res = 0 
        def dfs(i, count):
            nonlocal res
            if count == numSelect:
                tmp = 0
                for row in matrix:
                    if sum(row) == 0:
                        tmp += 1
                res = max(res, tmp)
                return 
            if i == n:
                return 

            dfs(i + 1, count)
            mask = 0
            # print(matrix, mask)
            for row in range(m):
                if matrix[row][i] == 1:
                    mask = mask | (1 << row)
                    matrix[row][i] = 0
            # print(matrix, mask)
            dfs(i + 1, count + 1)
            for row in range(m):
                if mask & (1 << row):
                    matrix[row][i] = 1
            # print(matrix)
            
        dfs(0, 0)
        return res
            
            