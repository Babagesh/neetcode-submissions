# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Preorder goes middle, left, right, m
        # In order goes left, middle, right
        hashmap = {}
        for index, num in enumerate(inorder):
            hashmap[num] = index

        def traverse(prestart, preend, instart, inend):
            if prestart > preend or instart > inend:
                return None
            root_val = preorder[prestart]
            root = TreeNode(root_val)
            mid = hashmap[root_val]
            left_size = mid - instart
            root.left = traverse(prestart + 1, prestart + left_size, instart, mid - 1)
            root.right = traverse(prestart + 1 + left_size, preend, mid + 1, inend)
            return root
        return traverse(0, len(preorder) - 1, 0, len(inorder) - 1)
        
        
