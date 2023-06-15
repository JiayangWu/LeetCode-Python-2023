class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)

        stack = []
        larger_number_distance = [inf for _ in arr]
        # find a number where the next larger than it number appears k
        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] < num:
                top = stack[-1]
                larger_number_distance[top] = i - top
                stack.pop()
            stack.append(i)  

        # print(larger_number_distance)
        for i, d in enumerate(larger_number_distance):
            if not i and d > k:
                return arr[i]
            elif i and d >= k:
                return arr[i]