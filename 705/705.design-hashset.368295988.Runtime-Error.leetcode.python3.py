"""
Design a HashSet without using any built-in hash table libraries.
To be specific, your design should include these functions:
add(value): Insert a value into the HashSet.
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.
Example:
MyHashSet hashSet = new MyHashSet();
hashSet.add(1);
hashSet.add(2);
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);
hashSet.contains(2);    // returns true
hashSet.remove(2);
hashSet.contains(2);    // returns false (already removed)
Note:
All values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashSet library.
"""


class MyHashSet1:
    def __init__(self):

        self.arr = [False] * 1000000

    def add(self, key):

        self.arr[key] = True

    def remove(self, key):

        self.arr[key] = False

    def contains(self, key):

        return self.arr[key]


class MyHashSet2:
    def __init__(self):

        self.cap = 10000
        self.size = 0
        self.set = [None] * self.cap

    def hash(self, key):
        return key % self.cap

    def add(self, key):

        if self.contains(key):
            return
        hash_key = self.hash(key)
        if not self.set[hash_key]:
            self.set[hash_key] = []
        self.set[hash_key].append(key)

    def remove(self, key):

        if not self.contains(key):
            return
        hash_key = self.hash(key)
        self.set[hash_key].remove(key)

    def contains(self, key):

        hash_key = self.hash(key)
        if not self.set[hash_key]:
            return False
        for k in self.set[hash_key]:
            if k == key:
                return True
        return False

