class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        si = 0 # s_index

        for word in words:
            if s[si:si + len(word)] != word:
                return False
            si += len(word)
            if si == len(s):
                return True
        return False