class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        self.cache = {}

        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.lru = self.cache.pop(key)
            self.cache[key] = self.lru
            return self.lru
        else:
            return -1
        


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        
        if len(self.cache) >= self.capacity:
            
            oldest = next(iter(self.cache))
            self.cache.pop(oldest)
        
        self.cache[key] = value
        
        
        
