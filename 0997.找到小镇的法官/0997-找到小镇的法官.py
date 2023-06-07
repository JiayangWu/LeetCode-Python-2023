class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # a trust b - a -> b
        from collections import defaultdict
        indegree, outdegree = defaultdict(int), defaultdict(int)
        for a, b in trust:
            indegree[b] += 1
            outdegree[a] += 1

        # judge should have 0 outdegree and n - 1 indegree
        judge = -1
        for i in range(1, n + 1):
            if outdegree[i] == 0 and indegree[i] == n - 1:
                if judge == -1:
                    judge = i
                else:
                    return -1

        return judge
