# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()
        
        low = 1
        high = length-2
        
        ##finding peak
        while low != high:
            test_index = low + (high - low)//2
            
            if mountain_arr.get(test_index) < mountain_arr.get(test_index + 1):
                low = test_index + 1
            else:
                high = test_index
        
        peak_index = low
        
        #searching in increasing part (left of the subarray)
        low = 0
        high = peak_index
        
        while low < high:
            test_index = low + (high - low)//2
            
            if mountain_arr.get(test_index) < target:
                low = test_index + 1
            else:
                high = test_index
        
        if mountain_arr.get(low) == target:
            return low
        
        #searching in decreasing part (right of the subarray)
        low = peak_index + 1
        high = length - 1
        
        while low < high:
            test_index = low + (high - low)//2
            
            if mountain_arr.get(test_index) > target:
                low = test_index + 1
            else:
                high = test_index
        
        if mountain_arr.get(low) == target:
            return low
        
        
        return -1 #not found
        
            
                