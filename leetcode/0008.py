class Solution:
    def myAtoi(self, s: str) -> int:
        index = 0
        while index < len(s) and s[index] == ' ':
            index += 1

        sign = 1
        if index < len(s) and s[index] in "+-":
            if s[index] == "-":
                sign = -1
            index += 1

        value = 0
        while index < len(s) and s[index].isdigit():
            value = value * 10 + (ord(s[index]) - ord('0'))
            index += 1

        value = sign * value
        value = min(value, 2 ** 31 - 1)
        value = max(value, -2 ** 31)

        return value
