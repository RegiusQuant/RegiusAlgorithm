from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        result = 0

        def merge(arr1: List[int], arr2: List[int]):
            nonlocal result

            p1, p2 = 0, 0
            while p1 < len(arr1):
                while p2 < len(arr2) and arr1[p1] > 2 * arr2[p2]:
                    p2 += 1
                result += p2
                p1 += 1

            temp = []
            p1, p2 = 0, 0
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

        def mergeSort(nums: List[int]) -> List[int]:
            if len(nums) <= 1:
                return nums

            mid = len(nums) // 2
            a = mergeSort(nums[:mid])
            b = mergeSort(nums[mid:])
            return merge(a, b)

        mergeSort(nums)
        return result
