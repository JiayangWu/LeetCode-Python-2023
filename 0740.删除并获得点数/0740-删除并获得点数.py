class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dp = [0] * (1 + max(nums))

        from collections import Counter
        num2freq = Counter(nums)

        prev = None
        for i, num in enumerate(sorted(nums)):
            if prev:
                if num - prev > 1:
                    while prev < num - 1:
                        dp[prev + 1] = dp[prev]
                        prev += 1
                if num == prev:
                    continue

            dp[num] = max(dp[num - 1], dp[num - 2] + num * num2freq[num])
            prev = num

        print(dp)
        return max(dp)