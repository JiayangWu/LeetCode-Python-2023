# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def inorder(node):
            if not node:
                return []

            return inorder(node.left) + [node.val] + inorder(node.right)
        l = inorder(root)
        for i in range(len(l)):
            if i and l[i] <= l[i - 1]:
                return False
        return True