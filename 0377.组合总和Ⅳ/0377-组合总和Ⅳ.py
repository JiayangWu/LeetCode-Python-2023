class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # dp[i]=dp[i-nums[0]]+dp[i-nums[1]]+dp[i=nums[2]]+...
        dp = [0] * (1 + target)
        dp[0] = 1
        for i in range(target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        return dp[target]