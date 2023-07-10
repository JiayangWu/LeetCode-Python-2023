class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # use binary search to find a proper pos of x in arr
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == x:
                left = mid
                break
            elif arr[mid] < x:
                left = mid + 1
            elif arr[mid] > x:
                right = mid - 1
        pos = left

        count = 0
        res_left = []
        res_right = []
        p_left, p_right = pos - 1, pos
        while count < k and p_left >= 0 and p_right < len(arr):
            if abs(arr[p_left] - x) <= abs(arr[p_right] - x):
                res_left.append(arr[p_left])
                p_left -= 1
            else:
                res_right.append(arr[p_right])
                p_right += 1
            count += 1

        while count < k and p_left >= 0:
            res_left.append(arr[p_left])
            p_left -= 1
            count += 1

        while count < k and p_right < len(arr):
            res_right.append(arr[p_right])
            p_right += 1
            count += 1

        return res_left[::-1] + res_right

        
