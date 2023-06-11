class SnapshotArray:

    def __init__(self, n: int):
        self.cache = [[[-1, 0]] for _ in range(n)]
        self.i = 0

    def set(self, index, val):
        self.cache[index].append([self.i, val])

    def snap(self):
        self.i += 1
        return self.i - 1

    @lru_cache(maxsize=None)
    def get(self, index, snap_id):
        i = bisect.bisect(self.cache[index], [snap_id + 1]) - 1
        return self.cache[index][i][1]  
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)