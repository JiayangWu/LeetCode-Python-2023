class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, res = 0, 0
        zero_count = 0
        for right, num in enumerate(nums):
            # window [left, right]
            if num == 0:
                zero_count += 1
                while zero_count > k:
                    if nums[left] == 0:
                        zero_count -= 1
                    left += 1
            res = max(right - left + 1, res)
        return res