class Solution:
    def maxNumber(self, nums1, nums2, k):
        def max_number_single_array(nums, k):
            stack = []
            to_pop = len(nums) - k  # The number of elements to pop from the stack

            for num in nums:
                while to_pop > 0 and stack and stack[-1] < num:
                    stack.pop()
                    to_pop -= 1
                stack.append(num)

            return stack[:k]

        def merge(nums1, nums2):
            result = []
            i, j = 0, 0

            while i < len(nums1) and j < len(nums2):
                # Compare the two arrays and choose the larger element
                if nums1[i:] > nums2[j:]:
                    result.append(nums1[i])
                    i += 1
                else:
                    result.append(nums2[j])
                    j += 1

            # Append the remaining elements from both arrays
            result += nums1[i:]
            result += nums2[j:]

            return result

    
        result = []

        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            # Merge the two maximum numbers from each array
            candidate = merge(max_number_single_array(nums1, i), max_number_single_array(nums2, k - i))

            # Update the result if the new candidate is larger
            if candidate > result:
                result = candidate

        return result