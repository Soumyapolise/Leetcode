class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        cnt = 0
        
        #finding the common (most-significant) bits in both left and right numbers.
        while left != right:
            left >>= 1
            right >>= 1
            cnt += 1
            
        #eg 101, 111 -> left = right = 1, cnt = 2, then adding cnt number of 0's, to depict the number of non-common occurences, since this is AND operation, unless all are same - we'll get that result else, 0, so we'll just add cnt many 0's to our left(or right,  both are equal at this point)
        return left << cnt
    
        