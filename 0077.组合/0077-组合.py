class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n < 1:
            return

        res = []
        def dfs(i, path):
            if len(path) == k:
                res.append(path[:])
                return
            
            if i == n + 1:
                return

            dfs(i + 1, path) 
            path.append(i)
            dfs(i + 1, path)
            path.pop()

        dfs(1, [])
        return res
