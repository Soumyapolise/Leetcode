class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = [(startTime[i], endTime[i], profit[i]) for i in range(len(startTime))]
        jobs.sort(key=lambda x: x[1])

        dp = [[0, 0]]  # dp[i] = [max_profit, last_job_end_time]

        for i in range(len(jobs)):
            s, e, p = jobs[i]
            j = len(dp) - 1
            while j >= 0 and dp[j][1] > s:
                j -= 1
            if dp[j][0] + p > dp[-1][0]:
                dp.append([dp[j][0] + p, e])

        return dp[-1][0]