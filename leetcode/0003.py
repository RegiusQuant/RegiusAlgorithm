class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0

        table = set()
        left, right = 0, 0
        while right < len(s):
            while s[right] in table:
                table.remove(s[left])
                left += 1
            
            table.add(s[right])
            result = max(result, right - left + 1)
            right += 1

        return result
            