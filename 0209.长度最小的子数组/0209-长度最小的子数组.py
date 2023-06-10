class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #  two pointers
        # left, right = 0, 0 # [left, right)
        # s = 0
        # res = float("inf")
        # while right < len(nums):
        #     while right < len(nums) and s < target:
        #         s += nums[right]
        #         right += 1
        #         # print(left, right, s, nums[left: right])
        #         if s >= target:
        #             res = min(res, right - left)
            
        #     while s >= target:
        #         s -= nums[left]
        #         left += 1
        #         # print(left, right, s, nums[left: right])
        #         if s >= target:
        #             res = min(res, right - left)
        # return res if res <= len(nums) else 0

        left, s = 0, 0
        res = len(nums) + 1
        for right, num in enumerate(nums):
            s += num
            while s - nums[left] >= target:
                s -= nums[left]
                left += 1
            if s >= target:
                res = min(res, right - left + 1)
        return res if res <= len(nums) else 0