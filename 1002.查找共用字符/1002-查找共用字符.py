class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        s = [inf] * 27

        for word in words:
            c = Counter(word)
            for i in range(27):
                char = chr(ord("a") + i)
                s[i] = min(s[i], c[char])
        res = []
        for i in range(27):
            if s[i] < inf:
                res += chr(ord("a") + i)  * s[i]
        return res