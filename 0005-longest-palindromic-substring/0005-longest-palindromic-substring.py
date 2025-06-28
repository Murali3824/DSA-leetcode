class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandCenter(s,left,right):
            substring = ''
            max_len = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right-left+1 > max_len:
                    max_len = right-left+1
                    substring = s[left:right+1]
                left -= 1
                right += 1
            return substring
        result = ''

        for i in range(len(s)):
            odd = expandCenter(s,i,i)
            even = expandCenter(s,i,i+1)
            if len(odd) > len(result):
                result = odd
            if len(even) > len(result):
                result = even
        return result