from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        table = {x: i for i, x in enumerate(arr2)}
        arr1.sort(key=lambda x: (0, table[x]) if x in table else (1, x))
        return arr1
