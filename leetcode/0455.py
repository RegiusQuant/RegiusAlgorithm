from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        result = 0

        g.sort()
        s.sort()

        p = 0
        for x in g:
            while p < len(s) and s[p] < x:
                p += 1
            if p < len(s):
                result += 1
                p += 1
            else:
                break
        return result
