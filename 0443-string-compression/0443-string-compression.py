class Solution:
    def compress(self, chars: List[str]) -> int:
        res = 0
        i = 0
        j = 0
        
        while j<len(chars):
            num = []
            while j<len(chars) and chars[j] == chars[i]:
                j += 1
            count = j-i
            if count > 1:
                # print(count, chars)
                for n in str(count):
                    num.append(n)
                chars[0:len(chars)] = chars[0:i+1] + num + chars[j:]
                i += len(str(count))
                #print(chars[i], i, chars)
            else:
                chars[0:len(chars)] = chars[0:i+1] + chars[j:]
            i += 1
            j = i
            
        return len(chars)