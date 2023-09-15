class Solution:
    def reverse(self, x):
        if x >= 0:
            sign = 1
        else:
            sign = -1
            x = -x

        reversed_str = str(x)[::-1]
        reversed_int = int(reversed_str)

        if reversed_int > 2**31 - 1 or reversed_int < -(2**31):
            return 0

        return reversed_int * sign


# Example Testing
s = Solution()
answer = s.reverse(-123)
print(answer)
