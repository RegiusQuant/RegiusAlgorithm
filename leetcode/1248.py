from collections import Counter
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        result = 0

        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num % 2)

        counter = Counter([0])
        for x in prefix[1:]:
            result += counter[x - k]
            counter[x] += 1

        return result
