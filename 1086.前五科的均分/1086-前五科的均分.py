class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        id2min_heap = dict()

        for i, score in items:
            if i not in id2min_heap:
                id2min_heap[i] = [score]
            else:
                heapq.heappush(id2min_heap[i], score)
                if len(id2min_heap[i]) > 5:
                    heapq.heappop(id2min_heap[i])
        
        res = []
        for i, heap in id2min_heap.items():
            res.append([i, sum(heap) // 5])

        return sorted(res)

