class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        path = [0] * n

        def dfs(i, mask):
            if i == n:
                if path not in res:
                    res.append(path[:])
                return

            for j in range(n):
                if mask & (1 << j) == 0:
                    # nums[j] was never used
                    path[i] = nums[j]
                    dfs(i + 1, mask | (1 << j))

        dfs(0, 0)
        return res