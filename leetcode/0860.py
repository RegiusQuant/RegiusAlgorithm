from collections import Counter
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        counter = Counter()

        def exchange(bill: int) -> bool:
            while counter[10] > 0 and bill >= 10:
                bill -= 10
                counter[10] -= 1
            while counter[5] > 0 and bill >= 5:
                bill -= 5
                counter[5] -= 1
            return bill == 0

        for bill in bills:
            counter[bill] += 1
            bill -= 5
            if not exchange(bill):
                return False
        return True
