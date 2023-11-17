class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        ignored, notignored, res = 0, 0, arr[0]
        for num in arr:
            if num >= 0:
                ignored += num
                notignored += num
            else:
                ignored = max(ignored + num, notignored)
                notignored += num
                
            res = max([res, ignored if ignored != 0 else -math.inf, notignored if notignored != 0 else -math.inf])
            if ignored < 0: ignored = 0
            if notignored < 0: notignored = 0
        return max(res, max(arr))    