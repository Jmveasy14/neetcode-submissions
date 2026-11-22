class Node:
    def __init__(self,key = 0, value = 0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def addtofront(self,node):
        first = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = first
        first.prev = node


    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.addtofront(node)
        return node.value

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.addtofront(node)
            return

        node = Node(key,value)
        self.cache[key] = node
        self.addtofront(node)
        if len(self.cache) > self.size:
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]
        

        
