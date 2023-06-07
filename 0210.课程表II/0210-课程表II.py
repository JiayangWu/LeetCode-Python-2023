class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict, deque
        indegree = defaultdict(int)
        src2des = defaultdict(list)

        for des, src in prerequisites:
            src2des[src].append(des)
            indegree[des] += 1
        
        # 1. find nodes with indegree == 0
        queue = deque([])
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        # 2. bfs deque
        res = []
        while queue:
            cur = queue.popleft()
            res.append(cur)

            for des in src2des[cur]:
                indegree[des] -= 1
                if indegree[des] == 0:
                    queue.append(des)
            
        return res if len(res) == numCourses else []
