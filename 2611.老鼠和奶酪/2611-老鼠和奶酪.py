class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        reward = [(reward1[i] - reward2[i], reward1[i], reward2[i]) for i in range(len(reward1))]
        reward.sort(key = lambda x: -x[0])

        res = 0
        for i in range(len(reward1)):
            if i <= k - 1:
                res += reward[i][1]
            else:
                res += reward[i][2]
        return res
