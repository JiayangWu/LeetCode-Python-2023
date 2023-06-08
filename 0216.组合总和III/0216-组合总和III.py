class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(i, path, path_sum):
            nonlocal n, k
            if len(path) == k and path_sum == n:
                res.append(path[:])
                return
            
            for j in range(i, 10):
                if path_sum + j <= n:
                    dfs(j + 1, path + [j], path_sum + j)

        dfs(1, [], 0)
        return res
