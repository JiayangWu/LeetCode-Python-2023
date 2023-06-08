class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        n = len(requests)
        self.res = 0
        def dfs(i, move_out, move_in, count):
            # print(move_in, move_out, i, count)
            if sorted(move_out) == sorted(move_in):
                self.res = max(self.res, count)
            if i == n:
                return
            
            dfs(i + 1, move_out, move_in, count)

            frm, to = requests[i]
            move_out.append(frm)
            move_in.append(to)
            dfs(i + 1, move_out, move_in, count + 1)
            move_out.pop()
            move_in.pop()
        
        dfs(0, [], [], 0)
        return self.res
