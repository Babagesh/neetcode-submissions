# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Define a function called check subtree which checks if a node is equal to head of subroot and then traverses from there to see if every node is hit. We would traverse through both the subtree which we call the checksubtree functio on and the actual subroot tree in the same way, until either one of them aren't the same, or we find that the subroot has run out of nodes and then in that case we return True

        def check_subtree(node, subTree):
            if not subTree and not node:
                return True
            if subTree and node:
                if node.val != subTree.val:
                    return False
                left_same = check_subtree(node.left, subTree.left)
                right_same = check_subtree(node.right, subTree.right)
                if left_same and right_same:
                    return True
                else:
                    return False
            else:
                return False

        found = check_subtree(root, subRoot)
        if found:
            return True
        if root.left:
            left_found = self.isSubtree(root.left, subRoot)
            if left_found:
                return True
        if root.right:
            right_found = self.isSubtree(root.right, subRoot)
            if right_found:
                return True
        return False
        