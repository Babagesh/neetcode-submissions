# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Need to have a tracker for each list
        # Have a dummy node to start off with
        # Iterate until left or right has reached the end
        # Add a node from one list(smaller one)
        # Move that pointer up
        # Compare nodes and see which one smaller, add the smaller one
        start = ListNode()
        tracker = start
        list1_tracker = list1
        list2_tracker = list2
        while list1_tracker and list2_tracker:
            list1_val = list1_tracker.val
            list2_val = list2_tracker.val
            if list1_val <= list2_val:
                tracker.next = list1_tracker
                list1_tracker = list1_tracker.next
                tracker = tracker.next
            else:
                tracker.next = list2_tracker
                list2_tracker = list2_tracker.next
                tracker = tracker.next
        while list1_tracker:
            tracker.next = list1_tracker
            tracker = tracker.next
            list1_tracker = list1_tracker.next
        
        while list2_tracker:
            tracker.next = list2_tracker
            tracker = tracker.next
            list2_tracker = list2_tracker.next
        return start.next



        