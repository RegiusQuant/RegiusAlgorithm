from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def search(depth: int, chosen: List[int]):
            if depth == len(nums):
                result.append(chosen)
                return

            search(depth + 1, chosen)
            search(depth + 1, chosen + [nums[depth]])

        search(0, [])
        return result
