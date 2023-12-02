class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = [[value, timestamp]]
        else:
            self.d[key] += [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.d:
            arr = self.d[key]
            for v, t in arr[::-1]:
                if t <= timestamp:
                    return v
        
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)