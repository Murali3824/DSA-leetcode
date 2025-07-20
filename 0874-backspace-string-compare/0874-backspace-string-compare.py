class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def backS(string):
            stack = []
            for char in string:
                if char != '#':
                    stack.append(char)
                else:
                    if stack:
                        stack.pop()
            return ''.join(stack)
        return backS(s) == backS(t)
