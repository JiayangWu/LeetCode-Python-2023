class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        grid_t = [list(col) for col in zip(*grid)]
        res = 0
        for row in grid:
            for col in grid_t:
                if row == col:
                    res += 1
        return res