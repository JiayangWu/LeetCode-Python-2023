class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = len(s)
        if not n:
            return []

        res = []
        def dfs(i, path):
            if i == n:
                res.append("".join(path))
                return
            
            if s[i].isdigit():
                dfs(i + 1, path + [s[i]])
            else:
                dfs(i + 1, path + [s[i].lower()])
                dfs(i + 1, path + [s[i].upper()])

        dfs(0, [])
        return res