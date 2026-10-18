# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([(root, 0)])
        nested_list = [[]]
        while queue:
            node, row = queue.popleft()
            left = node.left
            right = node.right
            if row >= len(nested_list):
                nested_list.append([])
            nested_list[row].append(node.val)
            if left:
                queue.append((left, row + 1))
            if right:
                queue.append((right, row + 1))
        return nested_list
