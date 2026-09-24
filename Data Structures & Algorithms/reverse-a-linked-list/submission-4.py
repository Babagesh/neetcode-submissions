# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # We have to make the next nodes next point to current
        # But we have to save the next nodes next and the next node to move onto
        # Then when we move o to the next 

        # We do this until next is None
        tracker = head
        if not tracker:
            return None
      
        tracker_next = tracker.next
        tracker.next = None
        while tracker:
            if tracker_next:
                tracker_next_next = tracker_next.next
                tracker_next.next = tracker
                tracker = tracker_next
                tracker_next = tracker_next_next
            else:
                break
        return tracker
