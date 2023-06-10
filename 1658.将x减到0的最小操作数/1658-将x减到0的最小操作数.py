class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target_window_s = sum(nums) - x
        left, s = 0, 0
        res = -1
        for right, num in enumerate(nums):
            s += num
            while left <= right and s > target_window_s:
                s -= nums[left]
                left += 1
            if s == target_window_s:
                res = max(res, right - left + 1)
        return len(nums) - res if res >= 0 else -1