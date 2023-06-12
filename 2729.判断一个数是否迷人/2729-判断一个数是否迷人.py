class Solution:
    def isFascinating(self, n: int) -> bool:
        s = str(n) + str(2 * n) + str(3 * n)
        if len(s) > 9:
            return False
        s = set(s)
        # print(s)
        return len(s) == 9 and "0" not in s
