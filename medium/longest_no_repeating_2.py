class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        found_chars = set()
        ans, i, j = 0, 0, 0
        while (i < n and j < n):
            if s[j] not in found_chars:
                found_chars.add(s[j])
                j += 1
                ans = max(ans, j - i)
            else:
                found_chars.remove(s[i])
                i += 1
        return ans

# i = 2
# j = 4
# ans = 3
# found_chars =  {c, a}