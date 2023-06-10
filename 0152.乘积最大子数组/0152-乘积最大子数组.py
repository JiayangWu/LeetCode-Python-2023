class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[1, 1] for _ in range(n + 1)]
        res = -inf 
        for i, num in enumerate(nums):
            dp[i + 1][0] = max(num, dp[i][0] * num, dp[i][1] * num)
            dp[i + 1][1] = min(num, dp[i][0] * num, dp[i][1] * num)
            res = max(res, dp[i + 1][0], dp[i + 1][1])
        print(dp)
        return res