class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = "".join([ch.lower() for ch in s if ch.isalnum()])
        return t[::-1] == t
