class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])
        res = []
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    i_down = i
                    while i_down < m and land[i_down][j] == 1:
                        i_down += 1
                    r2 = i_down - 1

                    j_right = j
                    while j_right < n and land[i][j_right] == 1:
                        j_right += 1
                    c2 = j_right - 1

                    res.append([i, j, r2, c2])

                    for ii in range(i, r2 + 1):
                        for jj in range(j, c2 + 1):
                            land[ii][jj] = 2
        return res