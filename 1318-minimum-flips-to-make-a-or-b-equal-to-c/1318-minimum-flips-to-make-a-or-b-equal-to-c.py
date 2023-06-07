class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        c = bin(c)[2:]
        a = bin(a)[2:]
        b = bin(b)[2:]
        combinations = {'00':1, '01':1, '10':1, '11':2}
        
        n =len(c)
        n1 = len(a)
        n2 = len(b)
        maxi = max(n, n1, n2)
        while n < maxi:
            c = '0' + c
            n+=1
        while n1 < maxi:
            a = '0' + a
            n1 += 1
        while n2 < maxi:
            b = '0' + b
            n2+=1
        count = 0
        print(a, b, c)
        for i in range(maxi):
            if (int(a[i]) or int(b[i])) != int(c[i]):
                count += combinations[a[i]+b[i]]
        
        return count