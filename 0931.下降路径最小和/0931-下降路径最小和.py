class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[inf] * n for _ in range(n)]
        dp[0] = matrix[0][:]
        for i in range(1, n):
            for j in range(n):
                x, y = i, j
                for yy in [y - 1, y, y + 1]:
                    if 0 <= yy < n:
                        dp[x][yy] = min(dp[x][yy], dp[x - 1][y] + matrix[x][yy])
        return min(dp[-1])