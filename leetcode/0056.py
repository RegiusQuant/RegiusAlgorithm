from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []

        intervals.sort()
        left, right = intervals[0]
        for interval in intervals:
            if interval[0] > right:
                result.append([left, right])
                left, right = interval
            else:
                right = max(right, interval[1])
        result.append([left, right])

        return result
