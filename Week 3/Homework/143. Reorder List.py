from typing import Optional

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # No reordering if there are 0,1 or 2 nodes
        if not head or not head.next or not head.next.next:
            return
        
        # Finding the middle using slow and faster pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reversing the second half of the list
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        
        # Now Merging the 2 halves
        # first is first half and rev_second is reversed second half
        first, rev_second = head, prev
        while rev_second:
            t1, t2 = first.next, rev_second.next
            first.next = rev_second
            rev_second.next = t1
            first, rev_second = t1,t2