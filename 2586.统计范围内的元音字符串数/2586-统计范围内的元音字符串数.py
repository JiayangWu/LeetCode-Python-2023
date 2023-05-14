class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowels = "aeiuo"
        res = 0

        for i in range(left, right + 1):
            word = words[i]
            if word and word[0] in vowels and word[-1] in vowels:
                res += 1
        return res 