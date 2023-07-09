class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        from collections import deque
        # i， j -> j, m - i - 1

        # time complexity: O(mn)
        # space complexity: O(n)

        m, n = len(box), len(box[0])

        for i in range(m):
            queue = deque()
            for j in range(n - 1, -1, -1):
                if box[i][j] == "#":
                    # check if we could move
                    if queue:
                        new_j = queue.popleft()
                        box[i][j], box[i][new_j] = box[i][new_j], box[i][j]
                        queue.append(j)
                elif box[i][j] == ".":
                    queue.append(j)
                elif box[i][j] == "*":
                    queue = deque()

        res = [["."] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                res[j][m - i - 1] = box[i][j]
        
        return res