class Solution:
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num
        return result


# Example Test
s = Solution()
nums = [2, 2, 1]
print(s.singleNumber(nums))
