# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # all lists are sorted
        # list_map key maps to the index of the `lists` object
        # {3: ListNode()}
        root = ListNode(-1)
        min_heap = []
        count = 0
        for lst in lists:
            if lst:
                heapq.heappush(min_heap, (lst.val, count, lst))
                count += 1

        curr = root
        count = 0
        while min_heap:
            _, _, lst = heapq.heappop(min_heap)
            if lst.next:
                heapq.heappush(min_heap, (lst.next.val, count, lst.next))
            curr.next = lst
            curr = curr.next
            count += 1

        curr.next = None
        return root.next