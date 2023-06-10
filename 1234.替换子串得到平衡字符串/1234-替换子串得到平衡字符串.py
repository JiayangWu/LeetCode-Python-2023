class Solution:
    def balancedString(self, s: str) -> int:
        c = Counter(s)
        target_count = len(s) // 4
        if all(c[x] == target_count for x in "QWER"):
            return 0
        left, res = 0, inf
        for right, char in enumerate(s):
            c[char] -= 1
            while left <= right and all(c[x] <= target_count for x in "QWER"):
                res = min(res, right - left + 1)
                c[s[left]] += 1
                left += 1
        return res