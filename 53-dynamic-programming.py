class Solution:
    def maxSubArray(self, nums):
        max_sum = current_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > current_sum + nums[i]:
                current_sum = nums[i]
            else:
                current_sum += nums[i]

            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum


# Example Test
s = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
answer = s.maxSubArray(nums)
print(answer)
