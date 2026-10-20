# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        global_left_max = float('-inf') # Every node in the left tree should be smaller than this value
        global_right_min = float('inf')  # Represent that every node in the right tree should be greater than this
        def check_valid(root, min_val, max_val):
            if not root:
                return True
            node_valid = root.val < max_val and root.val > min_val
            if not node_valid:
                return False
            return check_valid(root.left, min_val, root.val) and check_valid(root.right, root.val, max_val)
        return check_valid(root, global_left_max, global_right_min)