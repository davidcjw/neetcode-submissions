class ListNode:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:
    """
    head is the most recently used
    tail is the least recently used
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.tail.next, self.head.prev = self.head, self.tail
        self.keys = {}

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1
        
        self._moveNodeToHead(self.keys[key])
        return self.keys[key].value
    
    def _moveNodeToHead(self, node: ListNode) -> None:
        # disjoin node from prev and next nodes
        nodePrev, nodeNext = node.prev, node.next
        nodePrev.next, nodeNext.prev = nodeNext, nodePrev

        self._addNodeToHead(node)

    def _addNodeToHead(self, node: ListNode) -> None:
        # add node to head
        headPrev = self.head.prev
        headPrev.next, node.prev = node, headPrev
        node.next, self.head.prev = self.head, node

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            # Update key value and move to head
            node = self.keys[key]
            node.value = value
            self._moveNodeToHead(node)
            return
        
        newNode = ListNode(key, value)
        self.keys[key] = newNode
        self._addNodeToHead(newNode)
        if len(self.keys) > self.capacity:
            removed = self._evictLRU()
            self.keys.pop(removed)
    
    def _evictLRU(self) -> int:
        tailNext = self.tail.next
        self.tail.next = tailNext.next
        tailNext.next.prev = self.tail
        return tailNext.key
