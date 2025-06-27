class Solution:
    def reverseWords(self, s: str) -> str:
        x = s.split()
        x.reverse()
        new = ' '.join(x)
        return new

        