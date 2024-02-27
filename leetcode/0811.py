from collections import Counter
from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = Counter()
        for cpdomain in cpdomains:
            count, domain = cpdomain.split(" ")
            count = int(count)

            splitDomain = domain.split(".")
            counter[splitDomain[-1]] += count
            for i in range(2, len(splitDomain) + 1):
                counter[".".join(splitDomain[-i:])] += count

        result = []
        for k, v in counter.items():
            result.append(str(v) + " " + k)
        return result
