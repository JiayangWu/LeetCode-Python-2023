class Solution:
    def flipChess(self, chessboard: List[str]) -> int:
        m, n = len(chessboard), len(chessboard[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if chessboard[i][j] == ".":
                    res = max(res, self.bfs(chessboard, i, j, m, n))
        return res

    def bfs(self, chessboard, i, j, m, n):
        from collections import deque
        di = [1, -1, 0, 0, 1, 1, -1, -1]
        dj = [0, 0, 1, -1, 1, -1, 1, -1]
        chessboard = [list(row) for row in chessboard]
        queue = deque([(i, j)])
        res = 0
        while queue:
            i, j = queue.popleft()
            chessboard[i][j] = "X"
            for k in range(8):
                ii, jj, whites = i + di[k], j + dj[k], []
                while 0 <= ii < m and 0 <= jj < n:
                    if chessboard[ii][jj] == ".":
                        break
                    elif chessboard[ii][jj] == "O":
                        whites.append((ii, jj))
                    elif chessboard[ii][jj] == "X":
                        res += len(whites)
                        for iii, jjj in whites:
                            chessboard[iii][jjj] = "X"
                        queue.extend(whites)
                        break
                    ii, jj = ii + di[k], jj + dj[k]
        return res
                
