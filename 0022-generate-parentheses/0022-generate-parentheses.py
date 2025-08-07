class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def generate(s='', open=0, close=0):
            if len(s) == 2 * n:
                result.append(s)
                return
            if open < n:
                generate(s + '(', open + 1, close)
            if close < open:
                generate(s + ')', open, close + 1)

        generate()
        return result