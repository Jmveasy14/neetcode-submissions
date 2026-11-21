class Node:
   def __init__(self,key = 0,value = 0):
    self.prev = None
    self.next = None
    self.key = key
    self.value = value




class LRUCache:

    def _remove(self,node):
        node.next.prev = node.prev
        node.prev.next = node.next

    
    def add_to_front(self,node):
        first = self.head.next
        node.prev = self.head
        node.next = first
        first.prev = node
        self.head.next = node


    def __init__(self,capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

        

    def get(self, key: int) -> int:
        #we need to return the value and also note that it was used
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self.add_to_front(node)
            return node.value
        else:
            return -1            
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self.add_to_front(node)
        
        elif key not in self.cache:
            new_node = Node(key,value)
            self.cache[key] = new_node
            self.add_to_front(new_node)

            if len(self.cache) > self.capacity:
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
                


        
        
