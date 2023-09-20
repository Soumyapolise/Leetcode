class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total_sum = sum(nums)
        target_sum = total_sum - x

        if target_sum < 0:
            return -1  # It's not possible to reduce x to zero

        max_length = -1
        current_sum = 0
        left = 0

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum > target_sum:
                current_sum -= nums[left]
                left += 1

            if current_sum == target_sum:
                max_length = max(max_length, right - left + 1)

        return len(nums) - max_length if max_length != -1 else -1