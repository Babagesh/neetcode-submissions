# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Could traverse through the tree, have a min heap of length k and add to that min heap, and anytime minheap size is over take off the biggest element. Then at the end return the last element in the array for the k value. The runtime for this would be O(n log n) 

        # Faster runtime solution would probably be to find the smallest element
        # After finding smallest element we go back k times
        # We need to in order to get the left, middle right traversal
        # We go left, get the kth number from there, and get our k 
        # We then go right, and we need to pass in the k with it
        self.smallest = root.val
        self.found = False
        def find_k(root, k_rank):
            if root == None:
                return k_rank
            left_rank = find_k(root.left, k_rank)
            current_rank = left_rank + 1
            if self.found == True:
                return -1
            if current_rank == k:
                self.smallest = root.val
                self.found = True
                return -1
            right_rank = find_k(root.right, current_rank)
            return right_rank
        find_k(root, 0)
           
        return self.smallest
