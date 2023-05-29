class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.lis = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        self.lis[carType-1] -= 1
        if self.lis[carType-1] < 0:
            return False
        return True


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)