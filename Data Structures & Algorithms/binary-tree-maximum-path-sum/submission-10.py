# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Do a traversal for every subtree, calculate the optimal sum of every subtree and then return that number
        # We can do an postorde traversal
        # We can store the max sum every time
        # We have to choose to add the current node to the left and right
        # If we use both left and right then that itself is a max, and we update the global max variable but we can't traverse it to the paret
        # We can only traverse either left or right to the parent
        self.total_sum = float('-inf')
        def get_sum(root):
            if root is None:
                return 0
            left = get_sum(root.left)
            right = get_sum(root.right)
            left_sum = root.val + left
            right_sum = root.val + right
            max_sum = max(left_sum, right_sum, root.val)
            both_sum = root.val + left + right
            self.total_sum = max(both_sum, self.total_sum, max_sum)
            return max_sum
        get_sum(root)
        return self.total_sum

        
