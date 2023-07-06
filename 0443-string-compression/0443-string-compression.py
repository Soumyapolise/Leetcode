class Solution:
    def compress(self, chars: List[str]) -> int:
        res = 0
        i = 0
        j = 0
        s = []
        while j<len(chars):
            num = []
            while j<len(chars) and chars[j] == chars[i]:
                j += 1
            count = j-i
            if count > 1:
                for n in str(count):
                    num.append(n)
                s += chars[i:i+1] + num
            else:
                s += chars[i]
            i = j
            
            
        chars[0:len(chars)] = s[0:len(s)]
        return len(chars)