from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []

        counterS, counterP = Counter(), Counter(p)
        for i in range(len(s)):
            counterS[s[i]] += 1
            if i >= len(p):
                counterS[s[i - len(p)]] -= 1
            if counterS == counterP:
                result.append(i - len(p) + 1)

        return result
