class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for k in range(m)]
        dij = [[-1, 1], [0, 1], [1, 1]]
        
        for col in range(n):
            for row in range(m):
                if not col or dp[row][col] != 0:
                    for d in dij:
                        i, j = row + d[0], col + d[1]                        
                        if self.nodeInMatrix(i, j, m, n) and grid[i][j] > grid[row][col]:
                            dp[i][j] = max(dp[i][j], dp[row][col] + 1)
        
        return max([max(row) for row in dp])


    def nodeInMatrix(self, row, col, m, n):
        return 0 <= row < m and 0 <= col < n