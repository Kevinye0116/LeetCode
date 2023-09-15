class Solution:
    def convert(self, s, numRows):
        if numRows <= 1:
            return s

        rows = [""] * numRows
        curRow = 0
        goingdown = False

        for char in s:
            rows[curRow] += char
            if curRow == 0 or curRow == numRows - 1:
                goingdown = not goingdown
            curRow += 1 if goingdown else -1
        result = "".join(rows)
        return result


# Example Testing
a = Solution()
s = "PAYPALISHIRING"
numrows = 3
answer = a.convert(s, numrows)
print(answer)
