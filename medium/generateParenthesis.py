class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(comb: str, abertos: int, fechados: int):
            if abertos == fechados == n:
                res.append(comb)
                return
            if abertos < n:
                backtrack(comb + "(", abertos + 1, fechados)
            if fechados < abertos:
                backtrack(comb + ")", abertos, fechados + 1)
        backtrack("", 0, 0)

        return res