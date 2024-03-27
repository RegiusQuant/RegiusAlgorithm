class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        table = [[0] * n for _ in range(n)]
        for i in range(n):
            table[i][i] = 1

        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1
                if s[left] == s[right]:
                    table[left][right] = table[left + 1][right - 1] + 2
                else:
                    table[left][right] = max(table[left + 1][right], table[left][right - 1])
        return table[0][n - 1]
