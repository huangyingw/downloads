class Node():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.pre = None


class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.pre = self.head
    key_to_node = {}

    def get(self, key):
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self.moveToTail(node)
            return node.val
        else:
            return -1

    def moveToTail(self, node):
        node.pre = self.tail.pre
        self.tail.next = node
        node.next = self.tail
        self.tail.pre = node

    def put(self, key, val):
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.val = val
            return
        node = Node(key, val)
        self.key_to_node[key] = node
        self.moveToTail(node)

