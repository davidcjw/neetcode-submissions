# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find middle of list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        curr = slow.next
        prev = slow.next = None
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev, curr = curr, nextNode

        # Interleave both halves
        dummy = ListNode(-1)
        dummy.next = head
        firstHalf = dummy.next
        secondHalf = prev
        while secondHalf:
            # a b c | d e f
            # a d b c | e f
            secondHalfNext = firstHalf.next  # b
            remainingSecondHalf = secondHalf.next # e
            firstHalf.next = secondHalf
            secondHalf.next = secondHalfNext

            secondHalf = remainingSecondHalf
            firstHalf = secondHalfNext
