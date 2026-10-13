# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            equal = p.val == q.val
            if equal:
                left_tree = self.isSameTree(p.left, q.left)
                right_tree = self.isSameTree(p.right, q.right)
                if left_tree and right_tree:
                    return True
                else:
                    return False
            else:
                return False
        elif not p and not q:
            return True
        else:
            return False