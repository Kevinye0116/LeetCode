class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index, current_combination):
            if index == len(digits):
                result.append(current_combination)
                return

            current_digit = digits[index]
            letters = mapping[current_digit]

            for letter in letters:
                backtrack(index + 1, current_combination + letter)

        result = []
        backtrack(0, "")
        return result


# Example usage
digits = "23"
s = Solution()
print(s.letterCombinations(digits))
