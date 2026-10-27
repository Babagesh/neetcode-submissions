# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    # Traverse the tree and add None whenever a None is encountered
    # Do bfs
    # Add the rows of nodes
    # For deserialize, there should be a mathematical formula traversing the array
    # We know that at each row the number of nodes doubles
    # 
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"
        data = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                data.append(str(node.val))
                if node.left:
                    queue.append(node.left)
                else:
                    queue.append(None)
                if node.right:
                    queue.append(node.right)
                else:
                    queue.append(None)
            else:
                data.append("N")
        return ",".join(data)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(",")
        if not data:
            return None
        if data[0] == "N":
            return None
        root = TreeNode(val=data[0])
        queue = deque([root])
        i = 1
        while queue:
            node = queue.popleft()
            if node == "N":
                continue
            else:
                left = data[i]
                right = data[i + 1]
                if left != "N":
                    node.left = TreeNode(val=left)
                    queue.append(node.left)
                
                if right != "N":
                    node.right = TreeNode(val=right)
                    queue.append(node.right)
                i += 2
        return root
    




