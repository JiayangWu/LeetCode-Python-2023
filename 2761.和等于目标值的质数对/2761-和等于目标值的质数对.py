class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        nums = self.findPrime(n)
        res = []
        left, right = 0, len(nums) - 1
        while left <= right:
            s = nums[left] + nums[right]
            if s == n:
                res.append([nums[left], nums[right]])
                right -= 1
            elif s > n:
                right -= 1
            else:
                left += 1
        return res

    def findPrime(self, n):
        res = [1] * (n + 1)

        for i in range(2, int(n ** 0.5) + 1):
            if res[i]:
                k = 2
                while k * i <= n:
                    res[i * k] = 0
                    k += 1
        
        return [i for i, x in enumerate(res) if x and i >= 2]