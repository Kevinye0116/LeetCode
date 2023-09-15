class Solution:
    def searchInsert(self, nums, target):
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
        return left


s = Solution()
answer = s.searchInsert([1, 3, 5, 6], 5)
print(answer)
