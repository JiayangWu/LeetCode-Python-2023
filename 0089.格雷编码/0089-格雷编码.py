class Solution:
    def grayCode(self, n: int) -> List[int]:
        # res = []
        # l = 2 ** n

        # def dfs(i, s, grey):
        #     nonlocal res
        #     if i == l:
        #         if bin(grey[0] ^ grey[-1])[2:].count("1") == 1:
        #             res = grey[:]
        #         return 
        #     if not res:
        #         for digit in s:
        #             if not i or (bin(grey[i - 1] ^ digit)[2:].count("1") == 1):
        #                     dfs(i + 1, s - {digit}, grey + [digit])

        # dfs(1, set(range(1, 2 ** n)), [0])
        # return res
        return [i ^ i >> 1 for i in range(2 ** n)]