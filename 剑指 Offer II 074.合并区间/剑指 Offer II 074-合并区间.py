class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals
        intervals.sort()

        left, right = intervals[0][0], intervals[0][1]
        res = []
        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]

            if start <= right:
                right = max(right, end)
            else:
                res.append([left, right])
                left, right = start, end
        res.append([left, right])
        return res