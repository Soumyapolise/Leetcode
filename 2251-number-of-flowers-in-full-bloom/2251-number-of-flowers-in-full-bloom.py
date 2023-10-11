class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        n = len(people)
        arr = []
        res = [0]*n
        p_idx = defaultdict(list)

        for start, end in flowers:
            arr.append((start, 0))
            arr.append((end+1, 1))

        for idx, time in enumerate(people):
            p_idx[time].append(idx)
        
        for k in p_idx.keys():
            arr.append((k, 2))

        arr.sort()

        flowers = 0
        for time, tf in arr:
            if tf == 0: flowers += 1
            elif tf == 1: flowers -= 1
            elif tf == 2:
                for idx in p_idx[time]: res[idx] = flowers
        return res
#         flowers.sort()
        
#         res = []
        
#         for p in people:
#             left, right = 1, len(flowers)
#             count = 0
            
#             while left <= right:
#                 mid = left + (right - left) // 2
#                 if flowers[mid - 1][1] <= p:
#                     count = mid  # Update count
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#             # count = 0
#             # for pair in flowers:
#             #     if pair[0] > p:
#             #         break
#             #     elif p <= pair[1]:
#             #             count += 1
            
#             res.append(count)
        
#         return res