# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return False
        if self.is_identical_tree(root, subRoot):
            return True
        # print(root, subRoot, root == subRoot)
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def is_identical_tree(self, tree1, tree2):
        if tree1 is None and tree2 is None:
            return True
        elif tree1 is None or tree2 is None:
            return False
        else:
            return (
                tree1.val == tree2.val
                and self.is_identical_tree(tree1.left, tree2.left)
                and self.is_identical_tree(tree1.right, tree2.right)
            )