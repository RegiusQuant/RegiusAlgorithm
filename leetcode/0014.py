from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLength = min(len(s) for s in strs)

        result = ""
        for i in range(minLength):
            flag = True
            for j in range(1, len(strs)):
                if strs[j][i] != strs[j - 1][i]:
                    flag = False
                    break
            if flag:
                result += strs[0][i]
            else:
                break

        return result
