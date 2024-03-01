from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        visit = [False] * len(nums)

        def search(depth: int, chosen: List[int]):
            if depth == len(nums):
                result.append(chosen)

            for i in range(len(nums)):
                if not visit[i]:
                    visit[i] = True
                    search(depth + 1, chosen + [nums[i]])
                    visit[i] = False

        search(0, [])
        return result
