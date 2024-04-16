class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        s, p = " " + s, " " + p
        
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for j in range(2, m + 1, 2):
            if p[j] == "*":
                dp[0][j] = True
            else:
                break

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[j].isalpha():
                    dp[i][j] = dp[i - 1][j - 1] and s[i] == p[j]
                elif p[j] == ".":
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j - 2]
                    if s[i] == p[j - 1] or p[j - 1] == ".":
                        dp[i][j] = dp[i][j] or dp[i - 1][j]

        return dp[n][m]
