class Solution:
    def removeElement(self, nums, val):
        left, right = 0, len(nums)

        while left < right:
            if nums[left] == val:
                nums[left] = nums[right - 1]
                right -= 1
            else:
                left += 1

        return right


# Example Test
s = Solution()
nums = [3, 2, 2, 3]
val = 3
print(s.removeElement(nums, val))
