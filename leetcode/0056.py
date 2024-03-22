from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []

        intervals.sort()
        left, right = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] > right:
                result.append([left, right])
                left, right = intervals[i]
            else:
                right = max(right, intervals[i][1])
        result.append([left, right])

        return result
