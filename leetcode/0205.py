class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        table = {}
        for c1, c2 in zip(s, t):
            if c1 not in table:
                table[c1] = c2
            elif table[c1] != c2:
                return False

        table = {}
        for c1, c2 in zip(t, s):
            if c1 not in table:
                table[c1] = c2
            elif table[c1] != c2:
                return False

        return True
