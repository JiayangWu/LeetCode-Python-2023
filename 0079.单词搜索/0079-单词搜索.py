class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = False
        di = [1, -1, 0, 0]
        dj = [0, 0, 1, -1]
        m, n = len(board), len(board[0])
        def dfs(x, y, index, visited):
            nonlocal res
            if index == len(word):
                res = True
                return 
            
            for k in range(4):
                xx, yy = x + di[k], y + dj[k]
                if 0 <= xx < m and 0 <= yy < n and (xx, yy) not in visited and board[xx][yy] == word[index]:
                    dfs(xx, yy, index + 1, visited | {(xx, yy)})
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    dfs(i, j, 1, {(i, j)})
        return res
            