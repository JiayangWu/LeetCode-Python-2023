class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # find a subarray where the product of every element in this subarry is less than k
        left, m = 0, 1
        res = 0
        for right, num in enumerate(nums):
            m *= num
            while left <= right and m >= k:
                # print(left, right, m, res, nums[left:right + 1])
                m //= nums[left]
                left += 1
            res += right - left + 1
        return res