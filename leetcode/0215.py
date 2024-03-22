import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]

        pivot = nums[random.randint(0, len(nums) - 1)]

        left = [x for x in nums if x < pivot]
        middle = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]

        if k <= len(right):
            return self.findKthLargest(right, k)
        if k <= len(right) + len(middle):
            return middle[0]
        return self.findKthLargest(left, k - len(right) - len(middle))
