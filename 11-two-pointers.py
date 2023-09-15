class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            w = right - left
            if height[left] > height[right]:
                h = height[right]
            else:
                h = height[left]
            area = w * h
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


# Example Test
s = Solution()
answer = s.maxArea([1, 1])
print(answer)
