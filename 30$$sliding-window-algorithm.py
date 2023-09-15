class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        words_len = word_len * len(words)
        word_count = {}

        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        result = []

        for i in range(word_len):
            left = i
            current_word_count = {}

            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j : j + word_len]

                if word in word_count:
                    if word in current_word_count:
                        current_word_count[word] += 1
                    else:
                        current_word_count[word] = 1

                    while current_word_count[word] > word_count[word]:
                        left_word = s[left : left + word_len]
                        current_word_count[left_word] -= 1
                        left += word_len

                    if j - left + word_len == words_len:
                        result.append(left)

                else:
                    current_word_count.clear()
                    left = j + word_len
        return result


# Example Test
a = Solution()
s = "barfoothefoobarman"
words = ["foo", "bar"]
print(a.findSubstring(s, words))
