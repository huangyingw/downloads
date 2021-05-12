class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.tail.prev = self.head
        self.head.next = self.tail
        self.int_to_node = {}

    def get(self, key):
        if key not in self.int_to_node:
            return -1
        node = self.int_to_node[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        self.moveToTail(node)
        return node.value

    def put(self, key, value):
        if self.get(key) != -1:
            self.int_to_node[key].value = value
            return
        if len(self.int_to_node) == self.capacity:
            self.int_to_node.pop(self.head.next.key)
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
        insert = Node(key, value)
        self.int_to_node[key] = insert
        self.moveToTail(insert)

    def moveToTail(self, current):
        current.prev = self.tail.prev
        current.prev.next = current
        current.next = self.tail
        self.tail.prev = current

