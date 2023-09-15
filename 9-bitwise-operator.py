class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s[:len(s) >> 1] ==  s[ : - (len(s) >> 1) - 1: -1]
    

s = Solution()
print(s.isPalindrome(121))