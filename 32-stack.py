class Solution:
    def longestValidParentheses(self, s):
        stack = []
        start = -1
        max_length = 0

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                if not stack:
                    start = i
                else:
                    stack.pop()
                    if not stack:
                        max_length = max(max_length, i - start)
                    else:
                        max_length = max(max_length, i - stack[-1])

        return max_length


# Example Test
a = Solution()
s = "(()"
answer = a.longestValidParentheses(s)
print(answer)
