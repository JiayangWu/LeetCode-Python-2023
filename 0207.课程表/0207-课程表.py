class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topo sort
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
        learned_course = 0
        while queue:
            cur = queue.popleft()
            learned_course += 1

            for des in src2des[cur]:
                indegree[des] -= 1
                if indegree[des] == 0:
                    queue.append(des)
            
        return numCourses == learned_course
