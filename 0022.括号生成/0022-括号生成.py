class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(left, right, path):
            if left == right == 0:
                res.append(path[:])

            if left:
                dfs(left - 1, right, path + "(")
            if left < right:
                dfs(left, right - 1, path + ")")
        dfs(n, n, "")
        return res