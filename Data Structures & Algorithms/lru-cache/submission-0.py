class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val

        self.next, self.prev = None, None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        prev = self.right.prev
        node.prev = prev
        prev.next = node
        node.next = self.right
        self.right.prev = node
    

    def delete(self, node): 
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p




    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.delete(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val
        

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.delete(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.delete(lru)
            del self.cache[lru.key]