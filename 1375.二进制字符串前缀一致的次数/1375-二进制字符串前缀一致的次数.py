class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        max_step = 0
        res = 0

        for i, f in enumerate(flips):
            max_step = max(max_step, f)
            if max_step == i + 1:
                res += 1
        return res