class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        n1 = len(str(low))
        n2 = len(str(high))
        res = []
        
        for k in range(n1, n2+1):
            val = ""
            i = 1
            while val == "" or len(str(val)) < k:
                val += str(i)
                i += 1
            val = int(val)
            while val < int("9"*k) and (int(str(val)[0]) + len(str(val))) < 11 and val <= high:
                if val >= low:
                    res.append(val)
                val += int("1"*k)
        
        return res
        