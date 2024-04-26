from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        p = n - k % n
        nums[:] = nums[p:] + nums[:p]
