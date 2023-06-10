class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        queries = map(self.f, queries)
        words = sorted(map(self.f, words))
        res = []
        for q in queries:
            # left will finally point out to the first element that's greater than q
            left, right = 0, len(words) - 1
            while left <= right:
                # when this loop ends, left == right + 1
                mid = (left + right) // 2
                if words[mid] > q:
                    right = mid - 1
                elif words[mid] == q:
                    left = mid + 1
                else:
                    left = mid + 1
            # print(left, right)
            res.append(len(words) - left)
        return res



    
    def f(self, s):
        from collections import Counter
        c = Counter(s)

        for char in "abcdefghijklmnopqrstuvwxyz":
            if char in c:
                return c[char]