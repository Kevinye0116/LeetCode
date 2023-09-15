class Solution:
    def lengthOfLastWord(self, s):
        s = s.strip()

        if not s:
            return 0

        end = len(s) - 1
        while end >= 0 and s[end] != " ":
            end -= 1

        length = len(s) - 1 - end
        return length


# Example Testing
a = Solution()
s = "Hello World"
print(a.lengthOfLastWord(s))
