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
        # Head is the most recently used
        self.tail.next, self.head.prev = self.head, self.tail

    def moveNodeToHead(self, node):
        # 1) decouple node from current position
        nodePrev, nodeNext = node.prev, node.next
        nodePrev.next, nodeNext.prev = nodeNext, nodePrev

        # 2) move node to head
        self.insertHead(node)
    
    def insertHead(self, node):
        headPrev = self.head.prev
        headPrev.next, node.prev = node, headPrev
        self.head.prev, node.next = node, self.head
    
    def popTail(self):
        # remove LRU node from key map and linked list
        tailNext = self.tail.next
        self.keys.pop(tailNext.key)
        self.tail.next, tailNext.next.prev = tailNext.next, self.tail

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1
        
        curr = self.keys[key]
        self.moveNodeToHead(curr)
        return curr.val

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            curr = self.keys[key]
            curr.val = value
            self.moveNodeToHead(curr)
            return
        
        newNode = ListNode(key, value)
        self.keys[key] = newNode
        self.insertHead(newNode)
        if len(self.keys) > self.capacity:
            self.popTail()
