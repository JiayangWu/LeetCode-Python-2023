from heapq import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        num2freq = Counter(nums)
        min_heap = []
        # num_and_freq = []
        for num, freq in num2freq.items():
            # num_and_freq.append((num, freq))
            if len(min_heap) < k:
                heappush(min_heap, (freq, num))
            else:
                heappushpop(min_heap, (freq, num))
        # print(min_heap)
        return [pair[1] for pair in min_heap]


    
        
        
