class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        return n - self.numUniqueDigitsNum(n) 

    def numUniqueDigitsNum(self, num):
        s = str(num)
        n = len(s)
        @cache
        def dfs(i, mask, is_limit, is_num):
            if i == n:
                return int(is_num)
            res = 0
            if not is_num:
                res = dfs(i + 1, mask, False, is_num)
            up = int(s[i]) if is_limit else 9
            for d in range(1 - int(is_num), up + 1):
                if mask & 1 << d == 0:
                    res +=dfs(i + 1, mask|1 << d, is_limit and d == up, True)
            return res
        
        return dfs(0, 0, True, False)