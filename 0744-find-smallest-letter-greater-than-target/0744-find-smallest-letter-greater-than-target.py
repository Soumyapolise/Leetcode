class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        i = 0
        j = len(letters)-1
        
        while i<=j:
            mid = i + (j-i)//2
            if letters[mid] > target:
                if letters[mid-1] <= target:
                    return letters[mid]
                else:
                    j = mid-1
            else:
                i = mid + 1
        
        return letters[0]