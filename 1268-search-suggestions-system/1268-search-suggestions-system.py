class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        
        res = []
        i = 0
        for ch in searchWord:
            lis = []
            idx = []
            j = 0
            for p in products:
                if i < len(p) and p[i] == ch:
                    lis.append(p)
                    idx.append(j)
                j += 1
                
            if len(lis) >= 3:
                res.append(lis[0:3])
            else:
                res.append(lis)
                
            new_p = []
            for j in idx:
                new_p.append(products[j])
                
            products = new_p
            
            i += 1
        
        return res