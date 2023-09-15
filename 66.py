class Solution:
    def plusOne(self, digits):
        num_str = "".join(str(i) for i in digits)
        num = int(num_str)
        num += 1
        return [int(j) for j in str(num)]


s = Solution()
answer = s.plusOne([9])
print(answer)
