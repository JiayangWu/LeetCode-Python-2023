class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # pick several num to make their sum equal to sum(nums) // 2
        s, n = sum(nums), len(nums)
        if s % 2 != 0:
            return False
        # dfs(i, c) = dfs(i - 1, c) or dfs(i - 1, c - nums[i])
        @cache
        def dfs(i, c):
            if i < 0:
                return c == 0
            
            if c < nums[i]:
                return dfs(i - 1, c)
            return dfs(i - 1, c) or dfs(i - 1, c - nums[i])
        return dfs(n - 1, s // 2)