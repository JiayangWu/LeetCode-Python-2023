class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[float("inf") for _ in triangle[i]] for i in range(len(triangle))]
        dp[0][0] = triangle[0][0]
        for i in range(len(triangle)):
            for j in range(len(triangle[i])):
                if i + 1 < len(triangle):
                    dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + triangle[i + 1][j])
                    if j + 1 < len(triangle[i + 1]):
                        dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j] + triangle[i + 1][j + 1])
        # print(dp)
        return min(dp[-1])