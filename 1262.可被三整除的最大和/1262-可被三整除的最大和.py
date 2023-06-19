class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-inf] * 3 for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            num = nums[i - 1]
            for j in range(3):
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][(j - num) % 3] + num)
        return dp[-1][0]