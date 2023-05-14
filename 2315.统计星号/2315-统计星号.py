class Solution:
    def countAsterisks(self, s: str) -> int:
        between_bars = False
        res = 0
        for index, char in enumerate(s):
            if char == "|":
                between_bars = not between_bars
            if not between_bars and char == "*":
                res += 1
        return res