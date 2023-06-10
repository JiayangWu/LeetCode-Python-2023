class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict
        char2freq = defaultdict(int)  

        left, res = 0, 0
        for right, char in enumerate(s):
            char2freq[char] += 1
            while char2freq[char] > 1:
                char2freq[s[left]] -= 1
                left += 1
            # print(left, right, s[left: right + 1])
            res = max(res, right - left + 1)
        return res
                    