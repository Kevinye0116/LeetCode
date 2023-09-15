class Solution:
    def isHappy(self, n):
        def get_next(num):
            next_num = 0
            while num > 0:
                num, digit = divmod(num, 10)
                next_num += digit**2

            return next_num

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1


# Example Test
s = Solution()
n = 19
answer = s.isHappy(n)
print(answer)
