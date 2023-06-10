class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = citations[::-1]
        left, right = 0, len(citations) - 1
        while left <= right:
            mid = (left + right) // 2
            h = mid + 1
            if h < citations[mid]:
                left = mid + 1
            elif h == citations[mid]:
                left = mid + 1
            elif h > citations[mid]:
                right = mid - 1
        return left