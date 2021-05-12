class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.mapping = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        print('key in get --> %s' % (key))
        print('self.mapping --> %s' % (self.mapping))
        if key in self.mapping:
            node = self.mapping[key]
            self.remove(node)
            self.add(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.mapping:
            self.remove(self.mapping[key])
            print('self.mapping self.remove--> %s' % (self.mapping))
        node = Node(key, value)
        print('len(self.mapping) --> %s' % (len(self.mapping)))
        print('self.capacity --> %s' % (self.capacity))
        if len(self.mapping) > self.capacity:
            next_head = self.head.next
            self.remove(next_head)
            del self.mapping[next_head.key]
        self.add(node)
        self.mapping[key] = node
        print('key --> %s' % (key))
        print('self.mapping[key] --> %s' % (self.mapping[key].value))

    def add(self, node):
        tail = self.tail.prev
        tail.next = node
        self.tail.prev = node
        node.prev = tail
        node.next = self.tail

    def remove(self, node):
        prev_node = node.prev
        prev_node.next = node.next
        node.next.prev = prev_node

