class Solution:
    def punishmentNumber(self, n: int) -> int:
        res = 0
        for i in range(1, n + 1):
            i2 = i ** 2
            if self.canPartition(i):
                # print(i)
                res += i2
        return res

    def canPartition(self, n):
        n2 = n * n
        s = str(n2)
        l = len(s)
        res = False 
        def dfs(i, cur_sum):
            nonlocal res, n, n2
            if i == l:
                if cur_sum == n:
                    res = True
                return 
                
            if not res:
                for j in range(i, l):
                    cur_val = int(s[i:j + 1])
                    if cur_sum + cur_val <= n2:
                        dfs(j + 1, cur_sum + cur_val)
            
        dfs(0, 0)
        return res


