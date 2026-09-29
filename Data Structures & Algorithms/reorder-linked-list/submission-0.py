# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Have a left pointer at head and right pointer which traverses till end of list
        # From there save left right pointer as next to traverse too, set left to right pointer, update left to saved pointer, and update right one to the left. To make right go to one before we have to use recursion
        
        # Or we can simple use a stack, add the node, and once we visit we pop from the stack, and then we set right to the popped node
        self.left = head
        right = head
        def reach_end(right):
            if not right:
                return
            reach_end(right.next)
            if not self.left:
                return
            if self.left == right or self.left == right.next:
                self.left.next = None
                self.left = None
                return
            temp = self.left.next
            self.left.next = right
            right.next = temp
            self.left = temp
        reach_end(right)