class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        pos = []
        for i, num in enumerate(nums):
            if s[i] == "L":
                pos.append(num - d)
            else:
                pos.append(num + d)
        pos.sort()
        return self.get_pair_sum(pos) % (10 ** 9 + 7)

    def get_pair_sum(self, nums):
        pair_sum = 0
        prefix_sum = [0] * len(nums)

        # Compute prefix sum
        prefix_sum[0] = nums[0]
        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]

        # Calculate pair sum
        for i in range(1, len(nums)):
            pair_sum += nums[i] * i - prefix_sum[i-1]

        return pair_sum