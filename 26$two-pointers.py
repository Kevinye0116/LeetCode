class Solution:
    def removeDuplicates(self, nums):
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                j += 1
                nums[j - 1] = nums[i]
        return j


# Example Test
s = Solution()
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(s.removeDuplicates(nums))
