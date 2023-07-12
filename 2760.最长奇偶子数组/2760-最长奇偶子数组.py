class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        i = 0
        res = 0
        while i < len(nums):
            if nums[i] % 2 == 0 and nums[i] <= threshold:
                l, r = i, i + 1
                # search to the right
                remainder = 0
                while r < len(nums) and nums[r] % 2 != remainder and nums[r] <= threshold:
                    remainder = 1 - remainder
                    r += 1
                res = max(res, r - l)
                i = r
            else:
                i += 1
        return res