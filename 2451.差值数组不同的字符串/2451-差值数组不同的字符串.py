class Solution:
    def oddString(self, words: List[str]) -> str:
        diff = []
        for index, word in enumerate(words):
            t = []
            for i, char in enumerate(word):
                if i:
                    t.append(ord(char) - ord(word[i - 1]))
            diff.append([index, t])
        
        if diff[0][1] == diff[1][1]:
            same = diff[1][1]
            for d in diff:
                # print(d, same)
                if d[1] != same:
                    return words[d[0]]
        else:
            if diff[0][1] == diff[2][1]:
                return words[1]
            else:
                return words[0]
