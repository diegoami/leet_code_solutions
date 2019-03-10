class Solution:

    def expandAroundCenters(self, s, left, right):
        L, R = left, right
        while (L >= 0 and R < len(s) and s[L] == s[R]):
            L -= 1
            R += 1
        return R - L - 1

    def longestPalindrome(self, s: str) -> str:
        if (not s):
            return ""
        start, end = 0, 0
        for i in range(len(s)):
            len1 = self.expandAroundCenters(s, i, i)
            len2 = self.expandAroundCenters(s, i, i + 1)
            llen = max(len1, len2)
            if (llen > end - start):
                start = i - (llen - 1) // 2
                end = i + llen // 2

        return s[start:end + 1]


