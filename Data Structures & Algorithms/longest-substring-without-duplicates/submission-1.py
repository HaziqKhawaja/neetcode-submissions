class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        duplicates = {}
        left = 0
        for right in range(len(s)):
            if s[right] in duplicates:
                left = max(duplicates[s[right]]+1, left)
            duplicates[s[right]] = right
            max_length = max(max_length, right - left + 1)
        return max_length