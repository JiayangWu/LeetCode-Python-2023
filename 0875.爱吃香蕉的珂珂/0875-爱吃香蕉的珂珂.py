class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left <= right:
            mid = (left + right) // 2

            cur_time = 0
            for pile in piles:
                t, pile = divmod(pile, mid)
                if pile:
                    t += 1
                cur_time += t

            if cur_time > h:
                left = mid + 1
            else:
                right = mid - 1

        return left