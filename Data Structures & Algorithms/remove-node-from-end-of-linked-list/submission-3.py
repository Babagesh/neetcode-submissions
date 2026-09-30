# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Have a fast pointer and slow pointer
        # Keep the fast pointer n nodes ahead of slow
        # Whenever fast pointer reaches end wcheck where the slow pointer arrives
        if not head:
            return None
        fast = head
        slow = ListNode(next=head)
        slow_tracker = slow
        for i in range(n):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        # Now slow is at the node to remove
        # But we need to be one before the node to remove
        # Keep slow as dummy node
        next_node = slow.next.next
        slow.next = next_node
        return slow_tracker.next
       