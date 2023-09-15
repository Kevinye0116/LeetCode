class Solution:
    def strStr(self, haystack, needle):
        def get_next():
            for i in range(1, n):
                k = next_[i - 1]
                while needle[i] != needle[k]:
                    if k == 0:
                        # 比较到首位字符仍与当前字符needle[i]不一致，没有办法再往前找字符了。即needle[0,i]没有相同前后缀，next[i] = 0
                        k -= 1  # 为了和最后的next[i] = k + 1一致，k先减1等于-1，之后再加1变成0
                        break
                    else:
                        # needle[i]与needle[k]不一致，就要在needle[0, k - 1]中找一个更短的相同前后缀，即更新k = next[k - 1]
                        k = next_[k - 1]

                next_[i] = k + 1  # needle[i]的最长相同前后缀等于已有的k值再加1

        n = len(needle)
        next_ = [0] * n  # 初始化next数组
        get_next()  # 生成needle的next数组

        i = 0  # 遍历haystack的指针
        j = 0  # 指向needle的指针
        while i < len(haystack):
            if haystack[i] == needle[j]:
                # 字符匹配，两个指针都后移一位
                i += 1
                j += 1
            elif j == 0:
                # needle第一个字符就不匹配，haystack指针后移一位
                i += 1
            else:
                j = next_[j - 1]  # 找到已匹配的needle[0, j-1]的最长相同前后缀，更新j从这一位开始比较
            if j >= n:
                # needle匹配完成，返回匹配起点等于i - n（最后一位匹配完成后i也会后移一位，即匹配区间为[i - n, i - 1]长度为n）
                return i - n
        return -1  # 没有找到匹配子串，返回-1


s = Solution()
answer = s.strStr("hello", "ll")
print(answer)
