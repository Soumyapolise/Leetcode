class UndergroundSystem:

    def __init__(self):
        self.d = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.d[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        
        if self.d[id][0] in self.d:
            self.d[self.d[id][0]] += [[stationName, t - self.d[id][1]]]
        else:
            self.d[self.d[id][0]] = [[stationName, t - self.d[id][1]]]
        self.d.pop(id)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # print(self.d)
        sums, count = 0, 0
        for arr in self.d[startStation]:
            if arr[0] == endStation:
                sums += arr[1]
                count += 1
        return sums/count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)