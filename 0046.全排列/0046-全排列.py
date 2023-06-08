class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        path = [0] * n
        res = []
        def dfs(i, s):
            if i == n:
                res.append(path[:])
                return

            for char in s:
                path[i] = char
                dfs(i + 1, s - {char})

        dfs(0, set(nums))
        return res
                