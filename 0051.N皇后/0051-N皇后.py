class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols = [0] * n
        
        def is_valid(r, c):
            for R in range(r):
                C = cols[R]
                if R + C == r + c or R - C == r - c:
                    return False
            return True

        def dfs(r, s):
            if r == n:
                res.append(["." * c + "Q" + "." * (n - c - 1) for c in cols])
                return
            for c in s:
                if is_valid(r, c):
                    cols[r] = c
                    dfs(r + 1, s - {c})

        dfs(0, set(range(n)))
        return res