class Solution:
    def twoSum(self, nums, target):
        pos = []
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    pos.append(i)
                    pos.append(j)
                    return pos
                else:
                    j += 1
            i += 1


solution = Solution()
print(solution.twoSum([3, 2, 4], 6))
