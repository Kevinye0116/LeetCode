# Newton Iteration Method


class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x

        guess = x
        while guess * guess > x:
            guess = (guess + x // guess) // 2

        return guess


s = Solution()
answer = s.mySqrt(8)
print(answer)
