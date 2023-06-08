class Solution:
    def isAdditiveNumber(self, num: str) -> bool: 
        n = len(num)
        if n < 3:
            return False

        res = False
        def dfs(i, p_prev, prev, count):
            nonlocal res
            if i == n:
                if count >= 3:
                    res = True
                return
            
            if not res:
                up = n if num[i] != "0" else i + 1
                for j in range(i, up):
                    cur = int(num[i: j + 1])
                    if count <= 1 or cur == p_prev + prev:
                        # print(p_prev, prev, cur)
                        dfs(j + 1, prev, cur, count + 1)

        dfs(0, None, None, 0)
        return res