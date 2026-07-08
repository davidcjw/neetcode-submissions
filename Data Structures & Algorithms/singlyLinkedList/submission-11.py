class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        curr = self.head
        for i in range(index):
            if curr is None:
                return -1
            curr = curr.next
        return curr.val if curr else -1

    def insertHead(self, val: int) -> None:
        self.head = Node(val, self.head)
        
    def insertTail(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(val)

    def remove(self, index: int) -> bool:
        if not self.head:
            return False
        # special case: removing head
        if index == 0:
            self.head = self.head.next
            return True
        prev = self.head
        for i in range(index - 1):
            if prev.next is None:
                return False
            prev = prev.next
        if prev.next is None:
            return False
        prev.next = prev.next.next
        return True

    def getValues(self) -> List[int]:
        res = []
        curr = self.head
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res