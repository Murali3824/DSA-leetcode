class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        s_freq = [0]*26
        p_freq = [0]*26
        for char in p:
            p_freq[ord(char)-ord('a')] += 1
        for char in s[:len(p)]:
            s_freq[ord(char)-ord('a')] += 1
        if s_freq == p_freq:
            res.append(0)

        for i in range(len(p),len(s)):
            s_freq[ord(s[i])-ord('a')] += 1
            s_freq[ord(s[i-len(p)])-ord('a')] -= 1

            if s_freq == p_freq:
                res.append(i-len(p)+1)
        return res
