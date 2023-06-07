class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] = 1 + min(dp[i - coin[0], dp[i - coin[2], ...])
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(amount + 1):
            min_coin = float("inf")

            for coin in coins:
                if i >= coin and dp[i - coin] != 0:
                    min_coin = min(min_coin, dp[i - coin])
            
            if min_coin != float("inf"):
                dp[i] = 1 + min_coin
        # print(dp)
        return dp[amount] - 1