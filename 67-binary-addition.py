class Solution:
    def addBinary(self, a, b):
        carry = 0
        result = []
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0:
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0
            bit_sum = bit_a + bit_b + carry
            carry = bit_sum // 2
            bit_sum %= 2
            result.insert(0, str(bit_sum))
            i -= 1
            j -= 1
        if carry:
            result.insert(0, str(carry))
        return "".join(result)


s = Solution()
answer = s.addBinary("11", "1")
print(answer)
