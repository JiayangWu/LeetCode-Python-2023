class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        left, right = 0, len(citations) - 1
        while left <= right:
            mid = (left + right) // 2
            # h = mid + 1
            if mid + 1 < citations[mid]:
                left = mid + 1
            elif mid + 1 == citations[mid]:
                left = mid + 1
            elif mid + 1 > citations[mid]:
                right = mid - 1
        return left