class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                t = s[:left] + s[left + 1:]
                if t[::-1] == t:
                    return True
                t = s[:right] + s[right + 1:]
                if t[::-1] == t:
                    return True
                return False
        return True
