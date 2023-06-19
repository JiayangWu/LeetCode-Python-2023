class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        res = inf
        for i in range(1, len(nums)):
            val = nums[i] - nums[i - 1]
            if val < res:
                res = val
        return res