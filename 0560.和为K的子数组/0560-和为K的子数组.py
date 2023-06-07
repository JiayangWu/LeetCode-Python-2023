class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # from collections import defaultdict
        # prefix_sum = [0] + [0 for _ in nums]
        # for i, x in enumerate(nums):
        #     prefix_sum[i + 1] = prefix_sum[i] + x

        # val2count = defaultdict(int)

        # res = 0
        # for i, ps in enumerate(prefix_sum):
        #     if ps - k in val2count:
        #         res += val2count[ps - k]
        #     val2count[ps] += 1
        # return res
        from collections import defaultdict
        prefix_sum, res = 0, 0
        ps2count = defaultdict(int)
        ps2count[0] = 1
        for i, x in enumerate(nums):
            prefix_sum = prefix_sum + x
            if prefix_sum - k in ps2count:
                res += ps2count[prefix_sum - k]
            ps2count[prefix_sum] += 1
        return res