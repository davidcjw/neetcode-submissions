# Doubly linked list
class ListNode:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keys = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next, self.tail.prev = self.tail, self.head
        self.size = 0

    def moveToTail(self, key):
        nodeToMove = self.keys[key]
        nodePrev, nodeNext = nodeToMove.prev, nodeToMove.next
        nodePrev.next, nodeNext.prev = nodeNext, nodePrev
        self.addNodeToTail(nodeToMove)

    def addNodeToTail(self, node):
        prevTail = self.tail.prev
        prevTail.next, self.tail.prev = node, node
        node.prev, node.next = prevTail, self.tail

    def evictLRU(self):
        toEvict = self.head.next
        self.head.next, toEvict.next.prev = toEvict.next, self.head
        self.keys.pop(toEvict.key)
        self.size -= 1

    def get(self, key: int) -> int:
        if key in self.keys:
            self.moveToTail(key)
            return self.keys[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            self.keys[key].val = value
            self.moveToTail(key)
            return
        
        # new key: increase size first and check if exceed capacity
        self.size += 1

        # not in key map
        newNode = ListNode(key, value)
        self.keys[key] = newNode
        self.addNodeToTail(newNode)
        if self.size > self.capacity:
            self.evictLRU()
