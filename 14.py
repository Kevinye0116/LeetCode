# ChatGPT


class Solution:
    def longestCommonPrefix(self, strs):
        min_len = min(len(s) for s in strs)

        for i in range(min_len):
            current_char = strs[0][i]
            for s in strs:
                if current_char != s[i]:
                    return strs[0][:i]
        return strs[0][:min_len]


s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))
