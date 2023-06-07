class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # bfs from 4 edges, all found nodes are safe. Otherwise, overwrite with x
        from collections import deque
        if not board or not board[0]:
            return
        
        m, n = len(board), len(board[0])
        dxy = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        edges = [(i, j) for i in [0, m - 1] for j in range(n)] + [(i, j) for i in range(m) for j in [0, n - 1]]
        for i, j in edges:
            if board[i][j] == "O":
                queue = deque([(i, j)])
                board[i][j] = "S"
                
                while queue:
                    pair = queue.popleft()
                    x, y = pair[0], pair[1]

                    for k in range(len(dxy)):
                        xx = x + dxy[k][0]
                        yy = y + dxy[k][1]

                        if 0 <= xx < m and 0 <= yy < n and board[xx][yy] == "O":
                            board[xx][yy] = "S"
                            queue.append((xx, yy))

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "S":
                    board[i][j] = "O"
