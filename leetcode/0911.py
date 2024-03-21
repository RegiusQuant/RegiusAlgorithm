from collections import Counter
from typing import List


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        counter = Counter()

        top = persons[0]
        tops = [top]
        counter[top] += 1

        for person in persons[1:]:
            counter[person] += 1
            if counter[person] >= counter[top]:
                top = person
            tops.append(top)

        self.tops = tops
        self.times = times

    def q(self, t: int) -> int:
        left, right = 0, len(self.times) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if self.times[mid] <= t:
                left = mid
            else:
                right = mid - 1
        return self.tops[left]
