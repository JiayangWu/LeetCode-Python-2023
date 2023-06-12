class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # sum of numbers to add "+":  ps
        # sum of numbers to add "-":  ns = s - ps
        # ps - ns = target
        # ps - (s - ps) = target
        # 2 ps = target + s
        target += sum(nums)
        if target % 2 != 0 or target < 0:
            return 0
        return self.zero_one_backpack(nums, target // 2)


    def zero_one_backpack(self, nums, capacity):
        n = len(nums)

        @cache  
        def dfs(i, c):
            if i < 0:
                return 1 if c == 0 else 0
            if nums[i] > c:
                return dfs(i - 1, c)
            else:
                return dfs(i - 1, c - nums[i]) + dfs(i - 1, c)

        return dfs(n - 1, capacity)