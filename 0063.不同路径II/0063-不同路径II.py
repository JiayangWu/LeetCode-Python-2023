class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])

        dp = [[0 for j in range(n)] for i in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1:
                    if i >= 1:
                        dp[i][j] += dp[i - 1][j]
                    if j >= 1:
                        dp[i][j] += dp[i][j - 1]
        # print(dp)
        return dp[-1][-1] if grid[0][0] != 1 else 0