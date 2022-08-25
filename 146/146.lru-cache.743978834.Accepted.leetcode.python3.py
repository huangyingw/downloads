class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache(object):
    def __init__(self, capacity):

        self.capacity = capacity
        self.dict = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):

        if key in self.dict:
            n = self.dict[key]
            self._remove(n)
            self.dict[key] = n
            self._add(n)
            return n.val
        return -1

    def put(self, key, value):

        if key in self.dict:
            self._remove(self.dict[key])
        n = Node(key, value)
        self.dict[key] = n
        self._add(n)
        if len(self.dict.keys()) > self.capacity:
            t = self.head.next
            self._remove(t)
            del self.dict[t.key]

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

