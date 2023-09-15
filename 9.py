class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            list1 = list(map(int, str(x)))
            list1.reverse()
            num = int("".join(str(i) for i in list1))
            return num == x


s = Solution()
print(s.isPalindrome(121))
