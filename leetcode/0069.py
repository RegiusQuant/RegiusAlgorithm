class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left < right:
            mid = (left + right + 1) // 2
            if mid ** 2 <= x:
                left = mid
            else:
                right = mid - 1
        return left
