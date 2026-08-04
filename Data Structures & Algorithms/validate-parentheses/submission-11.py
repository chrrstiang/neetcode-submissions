class Solution:
    def isValid(self, s: str) -> bool:
        combos = set(["()", "[]", "{}"])
        opens = set(["{", "(", "["])
        closes = set(["}", ")", "]"])

        res = []
        for c in s:
            if c in opens:
                res.append(c)
            elif not c in opens and not res:
                return False
            else:
                combo = res.pop() + c
                if not combo in combos:
                    return False
        return len(res) == 0
