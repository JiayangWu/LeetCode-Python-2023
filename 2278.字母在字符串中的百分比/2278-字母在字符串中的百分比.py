class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return int(s.count(letter) * 100.0 / len(s)) if letter in s else 0