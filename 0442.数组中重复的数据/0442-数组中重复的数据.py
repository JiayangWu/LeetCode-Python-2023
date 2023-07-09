class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i, num in enumerate(nums):
            num = abs(num)
            target_pos = num - 1
            if nums[target_pos] < 0:
                res.append(num)
            else:
                nums[target_pos] *= -1
        return res