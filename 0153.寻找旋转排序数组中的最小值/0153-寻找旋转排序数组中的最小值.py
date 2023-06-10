class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        if nums[0] <= nums[-1]:
            return nums[0]
        while left <= right:
            mid = (left + right) // 2
            # print(nums[mid], left, right, mid)
            if nums[mid] > nums[0]:
                left = mid + 1
            elif nums[mid] == nums[0]:
                left = mid + 1
            elif nums[mid] < nums[0]:
                right = mid - 1
        return nums[left]