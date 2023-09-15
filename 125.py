class Solution:
    def isPalindrome(self, s):
        s1 = "".join([x for x in s.lower() if x.isalpha() or x.isdigit()])
        return s1 == s1[::-1]


# Example Test
a = Solution()
s = "0P"
print(a.isPalindrome(s))
