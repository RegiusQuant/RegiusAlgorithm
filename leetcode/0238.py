from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        prefixProduct = 1
        for i in range(len(nums)):
            result[i] = prefixProduct
            prefixProduct *= nums[i]

        suffixProduct = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suffixProduct
            suffixProduct *= nums[i]

        return result
