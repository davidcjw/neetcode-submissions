# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = l1
        s1 = ""
        while curr:
            s1 += str(curr.val)
            curr = curr.next

        curr = l2
        s2 = ""
        while curr:
            s2 += str(curr.val)
            curr = curr.next

        result = str(int(s1[::-1]) + int(s2[::-1]))[::-1]

        dummyHead = ListNode(-1)
        curr = dummyHead
        for c in result:
            newNode = ListNode(c)
            curr.next = newNode
            curr = curr.next
        
        return dummyHead.next
        