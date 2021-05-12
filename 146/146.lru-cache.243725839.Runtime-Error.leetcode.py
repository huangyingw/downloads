class LRUCache(object):
    class Node():
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.next = None
            self.pre = None

    def __init__(self, capacity):
        self.capacity = capacity
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.pre = self.head
    key_to_node = {}

    def get(self, key):
        if key in key_to_node:
            node = key_to_node[key]
            return node.val

    def put(self, key, val):
        if key in key_to_node:
            node = key_to_node[key]
            node.val = val
            return
        node = Node(val)
        key_to_node[key] = node
        moveToTail(node)

