class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        @cache
        def dfs(i, t):
            if t > i:
                return 0
            if i < 0:
                return inf

            return min(dfs(i - 1, t - 1), dfs(i - 1, t + time[i]) + cost[i])
        return dfs(n - 1, 0)