class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest_num = float("inf")

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if abs(current_sum - target) < abs(closest_num - target):
                    closest_num = current_sum

                if current_sum < target:
                    left += 1
                else:
                    right -= 1

        return closest_num


# Example Test
s = Solution()
nums = [-1, 2, 1, -4]
target = 1
answer = s.threeSumClosest(nums, target)
print(answer)
