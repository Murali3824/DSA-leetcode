class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(sub):
            #return sub == sub[::-1]
            left, right = 0, len(sub) - 1
            while left < right:
                if sub[left] != sub[right]:
                    return False
                left += 1
                right -= 1
            return True

        i, j = 0, len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return isPalindrome(s[i+1:j+1]) or isPalindrome(s[i:j])
        return True
