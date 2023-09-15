# The string would be valid as long as the brackets could be matched correctly.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {']': '[', ')': '(', '}': '{'}

        for char in s:
            if char in mapping:
                value = mapping.get(char)
                if value in stack:
                    stack.pop(stack.index(value))
                else:
                    return False
            else:
                stack.append(char)

        return not stack


# Example Testing
solution = Solution()
s = "({[}])"
print(solution.isValid(s))
