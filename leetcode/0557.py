class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s = [t[::-1] for t in s]
        return " ".join(s)
