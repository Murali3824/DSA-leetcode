class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expandCenter(left, right):

            substring = ""

            while left >= 0 and right < len(s) and s[left] == s[right]:

                substring = s[left:right+1]

                left -= 1
                right += 1

            return substring

        result = ""

        for i in range(len(s)):

            odd = expandCenter(i, i)

            even = expandCenter(i, i + 1)

            if len(odd) > len(result):
                result = odd

            if len(even) > len(result):
                result = even

        return result