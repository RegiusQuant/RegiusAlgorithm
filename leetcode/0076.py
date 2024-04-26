from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = s

        counterS, counterT = Counter(), Counter(t)
        left, right, count = 0, 0, 0

        while right < len(s):
            counterS[s[right]] += 1
            if counterS[s[right]] <= counterT[s[right]]:
                count += 1

            while left <= right and counterS[s[left]] > counterT[s[left]]:
                counterS[s[left]] -= 1
                left += 1

            if count == len(t) and right - left + 1 < len(result):
                result = s[left: right + 1]
            right += 1

        return result if count == len(t) else ""
