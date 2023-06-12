class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        left = 0
        res = 0
        nearby_count = 0
        for right, char in enumerate(s):
            if right:
                if char == s[right - 1]:
                    nearby_count += 1
                while nearby_count == 2:
                    if s[left] == s[left + 1]:
                        nearby_count -= 1
                    left += 1
            res = max(res, right - left + 1)
        return res