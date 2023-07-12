class Solution:
    def alternateDigitSum(self, n: int) -> int:
        sign = 1
        res = 0
        for digit in str(n):
            res += sign * int(digit)
            sign *= -1
        return res