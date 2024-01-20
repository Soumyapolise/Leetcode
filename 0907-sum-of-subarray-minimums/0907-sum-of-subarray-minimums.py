class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        n = len(arr)
        left = [-1] * n
        right = [n] * n
        stack = []

        # Finding nearest smaller element on the left
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        # Clear the stack for finding nearest smaller element on the right
        stack = []

        # Finding nearest smaller element on the right
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        # Calculate the sum of min(b) for all subarrays
        result = 0
        for i in range(n):
            result = (result + arr[i] * (i - left[i]) * (right[i] - i)) % mod

        return result