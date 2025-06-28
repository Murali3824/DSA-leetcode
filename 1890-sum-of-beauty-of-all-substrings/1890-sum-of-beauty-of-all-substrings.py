class Solution:
    def beautySum(self, s: str) -> int:
        def beuty(s):
            charfreq = Counter(s)
            return max(charfreq.values())-min(charfreq.values())
        
        res = 0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                substring = s[i:j]
                if len(substring)>2:
                    res+=(beuty(substring))
        return res
