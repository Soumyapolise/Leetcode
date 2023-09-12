class MyCalendar:

    def __init__(self):
        self.d = {}

    def book(self, start: int, end: int) -> bool:
        if self.d == {}:
            self.d[start] = end
            return True
        
        for s, e in self.d.items():
            if (start < s and end <= s) or (start >= e and end >= e):
                continue
            else:
                return False
        self.d[start] = end
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)