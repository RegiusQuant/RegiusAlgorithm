class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        t = [c for c in s if c.isalpha()][::-1]

        p = 0
        for i in range(len(s)):
            if s[i].isalpha():
                s[i] = t[p]
                p += 1
        return "".join(s)
