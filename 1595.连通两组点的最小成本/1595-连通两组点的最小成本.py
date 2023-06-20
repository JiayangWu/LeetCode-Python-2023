class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        n1,n2 = len(cost),len(cost[0])
        # 等价于成本矩阵中每行至少选择一个数,且最后每一行选择的列覆盖到了所有列时的最小成本
        # dp[i][j]当前覆盖的列状态为i,且当前处于第j行时的最小连接成本
        dp = [[10 ** 9 for _ in range(n1)] for _ in range(1 << n2)]
        for i in range(n2):
            dp[1 << i][0] = cost[0][i]
        
        for i in range(1 << n2):
            for j in range(1,n1):
                for c in range(n2):
                    # 选择第c列
                    if (i & (1 << c)):
                        dp[i][j] = min(dp[i][j],dp[i][j - 1] + cost[j][c])
                    else:
                        dp[i | (1 << c)][j] = min(dp[i | (1 << c)][j],dp[i][j - 1] + cost[j][c])
                # 对于没有选择的列在当前行进行更新
                for c in range(n2):
                    if not (i & (1 << c)):
                        dp[i | (1 << c)][j] = min(dp[i | (1 << c)][j],dp[i][j] + cost[j][c])

        return dp[(1 << n2) - 1][n1 - 1]           