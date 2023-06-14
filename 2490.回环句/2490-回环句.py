class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()

        for i, word in enumerate(words):
            if word[0] != words[i - 1][-1]:
                return False
        return True