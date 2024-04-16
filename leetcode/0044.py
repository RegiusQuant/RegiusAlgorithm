class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n  = len(s), len(p)
        s, p = " " + s, " " + p

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(1, n + 1):
            if p[j] == "*":
                dp[0][j] = True
            else:
                break

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j].isalpha():
                    dp[i][j] = dp[i - 1][j - 1] and s[i] == p[j]
                elif p[j] == "?":
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
        
        return dp[m][n]
