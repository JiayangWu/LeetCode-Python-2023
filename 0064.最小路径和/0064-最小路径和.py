class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])

        dp = [[float("inf") for j in range(n)] for i in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i + 1 < m:
                    dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + grid[i + 1][j])
                if j + 1 < n:
                    dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + grid[i][j + 1])
        # print(dp)
        return dp[-1][-1]