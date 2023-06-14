# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            res += abs(left_sum - right_sum)
            return left_sum + right_sum + node.val
        dfs(root)
        return res