class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        i = 0
        j = len(arr)-1
        
        while i<=j:
            mid = i + (j - i)//2
            # print(i, j, mid)
            if arr[mid-1] < arr[mid] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid+1] < arr[mid]:
                j = mid-1
            else:
                i = mid+1
        
        return i