class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        from collections import defaultdict, deque
        indegree = defaultdict(int)
        src2des = defaultdict(list)

        for src, des in edges:
            indegree[des] += 1
            indegree[src] += 1
            src2des[src].append(des)
            src2des[des].append(src)
        
        queue = deque()
        for node in range(n):
            if indegree[node] == 1:
                queue.append(node)
        
        remained_nodes = set(range(n))
        while len(remained_nodes) > 2:
            next_queue = deque()
            while queue:
                cur = queue.popleft()
                remained_nodes.remove(cur)

                for neighbor in src2des[cur]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 1:
                        next_queue.append(neighbor)
            queue = next_queue

        return list(remained_nodes)