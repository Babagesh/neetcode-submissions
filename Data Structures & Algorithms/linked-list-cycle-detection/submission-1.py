# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        cur = head
        next_node = head
        while next_node and next_node.next:
            next_node = next_node.next.next
            cur = cur.next
            if next_node == cur:
                return True
        return False
