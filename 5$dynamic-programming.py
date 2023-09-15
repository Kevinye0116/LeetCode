class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        start = 0
        max_length = 1

        for i in range(n):
            dp[i][i] = True

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        if length > max_length:
                            max_length = length
                            start = i

        return s[start : start + max_length]


# Example Testing
s = Solution()
answer = s.longestPalindrome("babad")
print(answer)
