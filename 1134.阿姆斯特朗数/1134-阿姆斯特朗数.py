class Solution:
    def isArmstrong(self, n: int) -> bool:
        k = len(str(n))
        s = sum([int(digit) ** k for digit in str(n)])
        return s == n