from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                for j in range(i + 1, len(digits)):
                    digits[j] = 0
                return digits
        return [1] + [0] * len(digits)
