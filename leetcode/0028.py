class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        b, p = 131, int(1e9 + 7)
        n, m = len(haystack), len(needle)

        table = [0] * (n + 1)
        for i in range(n):
            table[i + 1] = (table[i] * b + ord(haystack[i])) % p

        h, bm = 0, 1
        for i in range(m):
            h = (h * b + ord(needle[i])) % p
            bm = bm * b % p

        for i in range(n - m + 1):
            if (table[i + m] - table[i] * bm) % p == h and haystack[i: i + m] == needle:
                return i
        return -1
