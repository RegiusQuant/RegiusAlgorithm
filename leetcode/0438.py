from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []

        n, m = len(s), len(p)
        counterP = Counter(p)
        counterS = Counter()

        for i in range(n):
            counterS[s[i]] += 1
            if i >= m:
                counterS[s[i - m]] -= 1
            if counterS == counterP:
                result.append(i - m + 1)

        return result
