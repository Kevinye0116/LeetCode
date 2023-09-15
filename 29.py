class Solution:
    def divide(self, dividend, divisor):
        if divisor == 0:
            return 0
        if dividend == -(2**31) and divisor == -1:
            return 2**31 - 1

        if (dividend < 0) ^ (divisor < 0):
            sign = -1
        else:
            sign = 1

        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0
        while dividend >= divisor:
            temp_divisor = divisor
            multiple = 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            dividend -= temp_divisor
            quotient += multiple

        return sign * quotient


# Example Test
s = Solution()
dividend = 10
divisor = 3
print(s.divide(dividend, divisor))
