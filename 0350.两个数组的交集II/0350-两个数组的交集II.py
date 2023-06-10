class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        res = []
        for num, freq in c1.items():
            if num in c2:
                res += [num] * min(freq, c2[num])
        return res