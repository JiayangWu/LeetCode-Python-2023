class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i ** 2 for i in range(1, n + 1) if i ** 2 <= n]
        l = len(squares)

        # dfs(i, c) = min(dfs(i - 1, c), dfs(i, c - squares[i]) + 1)
        # dp[i + 1][c] = min(dp[i][c], dp[i + 1][c - squares[i] + 1])
        dp = [[inf] * (n + 1) for _ in range(l + 1)]
        dp[0][0] = 0
        
        for i in range(l):
            for c in range(n + 1):
                if c < squares[i]:
                    dp[i + 1][c] = dp[i][c]
                else:
                    dp[i + 1][c] = min(dp[i][c], dp[i + 1][c - squares[i]] + 1)

        return dp[l][n]

        
        # @cache
        # def dfs(i, c):
        #     if i < 0:
        #         return 0 if c == 0 else inf
        #     if c < squares[i]:
        #         return dfs(i - 1, c)  
        #     return min(dfs(i - 1, c), dfs(i, c - squares[i]) + 1)
        # return dfs(l - 1, n)