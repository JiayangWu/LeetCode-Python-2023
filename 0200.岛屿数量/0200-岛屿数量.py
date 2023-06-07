class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        def dfs(x, y, m, n):
            for k in range(len(dx)):
                xx, yy = x + dx[k], y + dy[k]

                if 0 <= xx < m and 0 <= yy < n and grid[xx][yy] == "1":
                    grid[xx][yy] = "0"
                    dfs(xx, yy, m, n)

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i, j, m, n) 
        return res


    