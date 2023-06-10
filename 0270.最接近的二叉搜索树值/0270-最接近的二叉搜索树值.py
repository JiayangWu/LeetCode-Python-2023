# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if not root:
            return -1
        if not root.left and not root.right:
            return root.val
        left, right = None, None
        if root.val >= target:
            left = self.closestValue(root.left, target)
            return self.getClosestValue(root.val, left, target)
        else:
            right = self.closestValue(root.right, target)
            return self.getClosestValue(root.val, right, target)


    def getClosestValue(self, val1, val2, target):
        if abs(val1 - target) < abs(val2 - target):
            return val1
        elif abs(val1 - target) == abs(val2 - target):
            return min(val2, val1)
        return val2
        
        
        
