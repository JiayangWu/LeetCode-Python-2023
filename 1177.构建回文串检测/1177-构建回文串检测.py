class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:

        index2counter = dict()
        counter = defaultdict(int)
        for i, char in enumerate(s):
            counter[char] += 1
            index2counter[i] = counter.copy()
        
        res = []
        for left, right, k in queries:
            counter = defaultdict(int)
            counter[s[left]] += 1
            # counter = index2counter[right] - index2counter[left] + {s[left]: 1}
            s1, s2 = set(index2counter[right]), set(index2counter[left])
            for key in  s1 | s2 :
                counter[key] += index2counter[right][key] - index2counter[left][key]
            odd_count = 0
            # print(counter)
            for key, val in counter.items():
                if val % 2 == 1:
                    odd_count += 1
            if (right - left + 1) // 2:
                res.append(odd_count // 2 <= k)
            else:
                res.append((odd_count - 1) // 2 <= k)
        return res