class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        from collections import defaultdict
        num2freq = defaultdict(int)
        for i, num in enumerate(nums):
            num2freq[num] += 1

        for f, t in zip(moveFrom, moveTo):
            if f != t:
                num2freq[t] += num2freq[f]
                num2freq.pop(f)
            
        return sorted(num2freq.keys())