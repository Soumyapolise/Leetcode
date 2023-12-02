class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = [[value, timestamp]]
        else:
            self.d[key] += [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        arr = self.d[key]
        i = 0
        j = len(arr)

        while i < j:
            mid = i + (j-i)//2
            if arr[mid][1] > timestamp:
                j = mid
            elif arr[mid][1] <= timestamp:
                i = mid + 1
        
        if j == 0:
            return ""
        else:
            return arr[j-1][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)