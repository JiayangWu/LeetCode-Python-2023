class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        # bfs + 染色
        from collections import deque
        if not land or not land[0]:
            return []

        m, n = len(land), len(land[0])

        def bfs(i, j):
            pond_size = 0
            queue = deque([(i, j)])
            
            while queue:
                i, j = queue.popleft()
                pond_size += 1
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        ii, jj = i + di, j + dj
                        if 0 <= ii < m and 0 <= jj < n and land[ii][jj] == 0:
                            land[ii][jj] = -1
                            queue.append((ii, jj))
            return pond_size

        res = []
        for i in range(m):
            for j in range(n):
                if land[i][j] == 0:
                    land[i][j] = -1
                    res.append(bfs(i, j))
        return sorted(res)