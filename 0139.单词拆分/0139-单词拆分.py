class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # indices = [0]
        # words = set(wordDict)

        # i = 0
        # while i < len(indices):
        #     index = indices[i]
        #     for word in words:
        #         if s[index:index + len(word)] == word:
        #             if index + len(word) == len(s):
        #                 return True
        #             indices.append(index + len(word))

        #     i += 1
        # return False
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        words = set(wordDict)
        for i, char in enumerate(s):
            for word in words:
                if i >= len(word) - 1:
                    # i == 3, word = 4 s[0:4]
                    if s[i - len(word) + 1:i + 1] == word:
                        # print(s[i - len(word) + 1:i + 1], word)
                        if dp[i - len(word) + 1]:
                            dp[i + 1] = max(dp[i + 1], dp[i - len(word) + 1] + 1)
        # print(dp)
        return dp[-1] > 0
