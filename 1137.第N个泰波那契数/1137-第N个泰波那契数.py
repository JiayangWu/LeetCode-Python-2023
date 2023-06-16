class Solution:
    def tribonacci(self, n: int) -> int:
        t0, t1, t2 = 0, 1, 1
        if n == 0:
            return t0
        elif n == 1:
            return t1
        elif n == 2:
            return t2
        
        cnt = 3
        while 1:
            res = t0 + t1 + t2
            if cnt == n:
                return res
            t0, t1, t2 = t1, t2, res
            cnt += 1