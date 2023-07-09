class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # increasing
        not_monotonic_increasing = False
        not_monotonic_decreasing = False
        for i, num in enumerate(nums):
            if i:
                if num < nums[i - 1]:
                    not_monotonic_increasing = True
        
                if num > nums[i - 1]:
                    not_monotonic_decreasing = True

        return not not_monotonic_decreasing or not not_monotonic_increasing