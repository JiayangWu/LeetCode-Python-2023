class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        di = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        res = 0

        def dfs(x, y):
            for k in range(4):
                xx = x + di[k]
                yy = y + dy[k]

                if 0 <= xx < m and 0 <= yy < n and grid[xx][yy] == 0:
                    grid[xx][yy] = 2
                    dfs(xx, yy)

        for i in range(m):
            for j in [0, n - 1]:
                if not grid[i][j]:
                    grid[i][j] = 2
                    dfs(i, j)

        for i in [0, m - 1]:
            for j in range(n):
                if not grid[i][j]:
                    grid[i][j] = 2
                    dfs(i, j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    grid[i][j] = 2
                    res += 1
                    dfs(i, j)
        return res