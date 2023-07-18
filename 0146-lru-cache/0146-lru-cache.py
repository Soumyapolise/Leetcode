class LRUCache:

    def __init__(self, capacity: int):
        self.num = capacity
        self.d = {}
        self.q = deque()
        
    def get(self, key: int) -> int:
        if key in self.d:
            if key in self.q:
                self.q.remove(key)
            self.q.append(key)
            return self.d[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d[key] = value
        else:
            self.d[key] = value
            
        if key in self.q:
            self.q.remove(key)
        self.q.append(key)
        
        if len(self.d) > self.num:
            catch = self.q.popleft()
            self.d.pop(catch)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)