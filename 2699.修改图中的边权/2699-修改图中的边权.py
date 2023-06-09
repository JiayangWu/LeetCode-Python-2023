class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        adj = collections.defaultdict(lambda:[])
        edges_a = []
        ans = []
        for u, v, w in edges:
            if w != -1:
                adj[u].append((v, w))
                adj[v].append((u, w))
                ans.append([u, v, w])
            else:
                edges_a.append([u, v])
        
        INF = 10**9+5
        dis = [INF] * n
        
        def dijkstra():
            for i in range(n): dis[i] = INF
            dis[source] = 0
            q = [(0, source)]
            vis = set()
            while q:
                d, u = heapq.heappop(q)
                if u in vis: continue
                vis.add(u)
                for v, w in adj[u]:
                    if d + w < dis[v]:
                        heapq.heappush(q, (d + w, v))
                        dis[v] = d + w
            # print(dis, adj)
        
        dijkstra()
        # print("-----", dis[destination], target)
        if dis[destination] < target: return []
        # print(dis[destination])
        
        i, m = 0, len(edges_a)
        # print(i, m)
        while i < m and dis[destination] > target:
            u, v = edges_a[i]
            i += 1
            adj[u].append((v, 1))
            adj[v].append((u, 1))
            dijkstra()
            
            if dis[destination] <= target:
                ans.append([u, v, 1 + target - dis[destination]])
                break
            ans.append([u, v, 1])
        
        # print(ans)
        if dis[destination] > target: 
            return []
            
        while i < m:
            u, v = edges_a[i]
            ans.append([u, v, INF])
            i += 1
        
        return ans