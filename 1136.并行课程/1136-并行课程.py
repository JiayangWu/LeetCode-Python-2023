class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        res = 0
        from collections import defaultdict, deque
        src2des = defaultdict(list)
        indegree = defaultdict(int)

        for prev, nxt in relations:
            src2des[prev].append(nxt)
            indegree[nxt] += 1

        queue = deque()
        for course in range(1, n + 1):
            if indegree[course] == 0:
                queue.append(course)
        
        learned_courses = 0
        while 1:
            next_queue = deque()
            res += 1
            while queue:
                cur = queue.popleft()
                learned_courses += 1

                for c in src2des[cur]:
                    indegree[c] -= 1
                    if indegree[c] == 0:
                        next_queue.append(c)  
            if not len(next_queue):
                return res if learned_courses == n else -1
            queue = next_queue
        

