# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1 -> 2 -> 3
        # 3 -> 2 -> 1
        cur = head
        prev = None
        while cur:
            if prev is None:
                node = ListNode(cur.val)
            else:
                node = ListNode(cur.val, prev)

            prev = node
            cur = cur.next
        
        return prev
