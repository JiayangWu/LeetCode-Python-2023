class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        if n == 0:
            return []

        res = []
        def dfs(i, path, path_sum):
            if path_sum == target:
                if sorted(path) not in res:
                    res.append(sorted(path))
                return

            if path_sum > target or i == n:
                return

            for digit in candidates[i:]:
                dfs(i, path + [digit], path_sum + digit)
        dfs(0, [], 0)
        return res
