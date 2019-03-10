class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_found, start = 1, 0
        found_chars = set()
        for idx in range(len(s)):
            char = s[idx]
            if char in found_chars:
                len_found = idx - start
                if (len_found > max_found):
                    max_found = len_found
                start = idx
                found_chars = set()
            found_chars.add(char)

        return max_found
