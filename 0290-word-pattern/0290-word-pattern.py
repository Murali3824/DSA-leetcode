class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        mapPW = {}
        mapWP = {}
        for i in range(len(pattern)):
            p = pattern[i]
            w = words[i]
            if ((p in mapPW and mapPW[p] != w) or (w in mapWP and mapWP[w] != p)):
                return False
            mapPW[p] = w
            mapWP[w] = p
        return True
