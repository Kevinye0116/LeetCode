class Solution:
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        if n <= 1:
            return n

        max_length = 0
        left = 0
        char_index = {}

        for right in range(n):
            if s[right] in char_index and char_index[s[right]] >= left:
                left = char_index[s[right]] + 1

            char_index[s[right]] = right
            max_length = max(max_length, right - left + 1)

        return max_length


# Example Testing
s = Solution()
answer = s.lengthOfLongestSubstring("dvdf")
print(answer)
