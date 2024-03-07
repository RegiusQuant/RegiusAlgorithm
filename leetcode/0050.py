class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1.0 / self.myPow(x, -n)

        temp = self.myPow(x, n // 2)
        result = temp * temp
        if n % 2 == 1:
            result *= x
        return result
