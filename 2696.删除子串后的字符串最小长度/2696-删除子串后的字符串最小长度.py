class Solution:
    def minLength(self, s: str) -> int:
        if "AB" not in s and "CD" not in s:
            return len(s)
        
        if "AB" in s:
            i = s.index("AB")
            return self.minLength(s[:i] + s[i + 2:])
        
        elif "CD" in s:
            i = s.index("CD")
            return self.minLength(s[:i] + s[i + 2:])