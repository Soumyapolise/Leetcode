class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        lis = ['']
        for ch in s:
            temp = []
            for item in lis:
                if ch.isalpha():
                    temp.append(item + ch)
                    temp.append(item + ch.swapcase())
                else:
                    temp.append(item + ch)
            
            lis = temp
        
        return lis