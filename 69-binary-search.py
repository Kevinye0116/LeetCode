# Binary Search


class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x

        left, right = 0, x // 2
        while left <= right:
            mid = (left + right) // 2
            mid_squared = mid * mid

            if mid_squared == x:
                return mid
            elif mid_squared < x:
                left = mid + 1
            else:
                right = mid - 1

        return right


s = Solution()
answer = s.mySqrt(8)
print(answer)
