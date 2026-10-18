# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # We do a search from Tree to each node to find each nodes ancestors
        # We make a set of the ancestors for one()
        # Then we go through the other trip in reverse and see if the ancestor or node is in that set
        p_path = self.getPath(root, p.val)
        q_path = self.getPath(root, q.val)
        max_length = max(len(p_path), len(q_path))
        ancestors = set() # Make set out of shorter path
        for i in range(max_length):
            q_index = len(q_path) - i - 1
            p_index = len(p_path) - i - 1
            if q_index >= 0 and p_index >= 0:
                q_anc = q_path[q_index]
                p_anc = p_path[p_index]
                q_anc_val = q_anc.val
                p_anc_val = p_anc.val
                if len(p_path) < len(q_path):
                    ancestors.add(p_anc_val)
                    if q_anc_val in ancestors:
                        return q_anc
                else:
                    ancestors.add(q_anc_val)
                    if p_anc_val in ancestors:
                        return p_anc
            elif len(p_path) == max_length:
                p_anc = p_path[p_index]
                p_anc_val = p_anc.val
                if p_anc_val in ancestors:
                    return p_anc
            elif len(q_path) == max_length:
                q_anc = q_path[q_index]
                q_anc_val = q_anc.val
                if q_anc_val in ancestors:
                    return q_anc


        

    def getPath(self, root, value):
        if root.val == value:
            return [root]
        elif root.val > value:
            return [root] + self.getPath(root.left, value)
        else:
            return [root] + self.getPath(root.right, value)