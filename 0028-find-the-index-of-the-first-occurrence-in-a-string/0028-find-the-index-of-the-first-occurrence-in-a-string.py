class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #return haystack.find(needle)
        n = len(haystack)
        m = len(needle)

        if m > n:
            return -1
        
        i = j = 0
        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == m:
                    return i - m
            else:
                i = i-j+1
                j = 0
        return -1
