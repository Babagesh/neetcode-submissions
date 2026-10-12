# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Go through lists, and call sort function to sort one list with another linkedlist
        # Loop through sorted list
        while len(lists) > 1:
            new_sorted = []
            if len(lists) % 2 != 0:
                new_sorted.append(lists[-1]) 
            for index in range(0, len(lists) - 1, 2):
            # Sort combined list with each incoming list
                sorted_list = self.sort_list(lists[index], lists[index + 1])
                new_sorted.append(sorted_list)
            lists = new_sorted
        if len(lists) >= 1:
            return lists[0]
        return None

    def sort_list(self, list1, list2): # Runs in O(k)
        head = ListNode()
        tracker = head
        l1ptr = list1
        l2ptr = list2
        # Go through list1 and list2
        # Compare list1 and list2 node
        # Whichever one is smaller append to tracker(tracker.next = smaller)
        # Then move the smaller pointer forward
        # Do this until ptr1 or ptr2 is at end
        # Once at end, iterate through remaining nodes in both lists

        while l1ptr and l2ptr:
            if l1ptr.val < l2ptr.val:
                smaller = l1ptr
                tracker.next = smaller
                tracker = tracker.next
                l1ptr = l1ptr.next
            elif l1ptr.val > l2ptr.val:
                smaller = l2ptr
                tracker.next = smaller
                tracker = tracker.next
                l2ptr = l2ptr.next
            else:
                tracker.next = l1ptr
                tracker = tracker.next
                l1ptr = l1ptr.next
                tracker.next = l2ptr
                tracker = tracker.next
                l2ptr = l2ptr.next
        while l1ptr:
            tracker.next = l1ptr
            tracker = tracker.next
            l1ptr = l1ptr.next
        while l2ptr:
            tracker.next = l2ptr
            tracker = tracker.next
            l2ptr = l2ptr.next
        return head.next
        

        