class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        MAPPING = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        n = len(digits)
        if n == 0:
            return []

        res = []
        def dfs(i, path):
            if i == n:
                res.append(path)
                return

            for digit in MAPPING[int(digits[i])]:
                dfs(i + 1, path + digit)
        dfs(0, "")
        return res