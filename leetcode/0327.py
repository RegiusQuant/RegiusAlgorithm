from typing import List


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        nums = [0] + nums
        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + nums[i]
        result = 0

        def merge(arr1: List[int], arr2: List[int], lower: int, upper: int) -> List[int]:
            nonlocal result

            left, right = 0, 0
            for i in range(len(arr1)):
                while left < len(arr2) and arr2[left] - arr1[i] < lower:
                    left += 1
                while right < len(arr2) and arr2[right] - arr1[i] <= upper:
                    right += 1
                result += right - left

            p1, p2, temp = 0, 0, []
            while p1 < len(arr1) and p2 < len(arr2):
                if arr1[p1] <= arr2[p2]:
                    temp.append(arr1[p1])
                    p1 += 1
                else:
                    temp.append(arr2[p2])
                    p2 += 1
            while p1 < len(arr1):
                temp.append(arr1[p1])
                p1 += 1
            while p2 < len(arr2):
                temp.append(arr2[p2])
                p2 += 1
            return temp

        def mergeSort(nums: List[int], lower: int, upper: int) -> List[int]:
            if len(nums) <= 1:
                return nums

            mid = len(nums) // 2
            arr1 = mergeSort(nums[:mid], lower, upper)
            arr2 = mergeSort(nums[mid:], lower, upper)
            return merge(arr1, arr2, lower, upper)

        mergeSort(nums, lower, upper)
        return result
