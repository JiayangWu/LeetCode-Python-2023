class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [num for num in nums]
        
        res = nums[0]
        for i, num in enumerate(nums):
            if i: 
                if dp[i - 1] > 0:
                    dp[i] = max(dp[i], num + dp[i - 1])
            res = max(dp[i], res)

        return res