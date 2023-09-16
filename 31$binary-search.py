class Solution:
    def searchRange(self, nums, target):
        def findLeft(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        def findRight(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1

            return right

        left_idx = findLeft(nums, target)
        right_idx = findRight(nums, target)

        if left_idx <= right_idx:
            return [left_idx, right_idx]
        else:
            return [-1, -1]


# Example Test
s = Solution()
nums = [5, 7, 7, 8, 8, 10]
target = 8
answer = s.searchRange(nums, target)
print(answer)
