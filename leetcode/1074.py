from collections import Counter
from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        result = 0

        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            total = [0] * n
            for j in range(i, m):
                for k in range(n):
                    total[k] += matrix[j][k]
                result += self.subarraySum(total, target)

        return result

    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0

        counter = Counter([0])
        count = 0
        for num in nums:
            count += num
            if count - k in counter:
                result += counter[count - k]
            counter[count] += 1

        return result
