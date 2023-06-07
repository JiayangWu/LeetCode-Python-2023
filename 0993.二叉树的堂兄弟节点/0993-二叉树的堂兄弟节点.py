# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # 层序遍历，如果同时在下一层出现且父亲不同，则是堂兄弟
        if not root:
            return False
        from collections import deque

        queue = [root]
        while queue:
            next_queue = []
            xin, yin = False, False
            for node in queue:
                if node.val == x:
                    xin = True
                if node.val == y:
                    yin = True
                if node.left and node.right:
                    if node.left.val == x and node.right.val == y or (node.right.val == x and node.left.val == y):
                        return False
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            
            if xin and yin:
                return True
            queue = next_queue[:]
        return False
                