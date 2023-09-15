class Solution:
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] != "*":
                    dp[i][j] = dp[i - 1][j - 1] and (
                        s[i - 1] == p[j - 1] or p[j - 1] == "."
                    )
                else:
                    dp[i][j] = dp[i][j - 2] or (
                        dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == ".")
                    )

        return dp[m][n]


# Example Test
s = "aa"
p = "a*"
x = Solution()
print(x.isMatch(s, p))
