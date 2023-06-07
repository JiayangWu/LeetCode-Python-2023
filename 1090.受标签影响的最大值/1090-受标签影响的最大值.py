class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        from collections import defaultdict
        label2count = defaultdict(int) 
        count = 0
        res = 0
        for v, l in sorted(zip(values, labels), reverse = True):
            if label2count[l] < useLimit:
                label2count[l] += 1
                res += v
                count += 1
            if count == numWanted:
                break
        return res

