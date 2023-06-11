class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        s = set()
        left, right = 0, len(nums) - 1
        while left <= right:
            s.add((nums[left] + nums[right]) / 2.0)
            left += 1
            right -= 1
        return len(s)