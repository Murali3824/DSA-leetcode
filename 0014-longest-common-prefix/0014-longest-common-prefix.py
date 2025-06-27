class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_word = min(strs)
        length = len(min(strs))
        res = ""
        for i in range(length):
            for word in strs:
                if shortest_word[i] == word[i]:
                    continue
                else:
                    return res
            res += word[i]
        return res


