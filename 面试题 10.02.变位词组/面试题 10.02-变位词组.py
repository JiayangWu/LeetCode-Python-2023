class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        d = defaultdict(list)

        for s in strs:
            d["".join(sorted(s))].append(s)

        return [val for key, val in d.items()]