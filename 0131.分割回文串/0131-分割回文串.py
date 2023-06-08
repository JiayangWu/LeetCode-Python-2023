class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s) 
        if n == 0:
            return []

        res = []
        def dfs(i, path):
            if i == n:
                res.append(path[:])
                return

            for j in range(i, n):
                substring = s[i:j + 1]
                if substring == substring[::-1]:
                    dfs(j + 1, path + [substring])
        dfs(0, [])
        return res