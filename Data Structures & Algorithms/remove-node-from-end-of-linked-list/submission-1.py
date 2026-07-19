# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        
        curr = head
        # 5; n=2 -> 4th
        # 5-2 = 3
        # 1 2 3 4 5
        prev = None
        for i in range(count-n):
            if i == count-n-1:
                prev = curr
            curr = curr.next
        
        if prev is None:
            return head.next

        prev.next = curr.next

        return head
