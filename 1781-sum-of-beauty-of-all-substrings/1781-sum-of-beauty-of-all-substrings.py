class Solution:
    def beautySum(self, s: str) -> int:

        total = 0
        n = len(s)

        for i in range(n):

            freq = {}

            for j in range(i, n):

                ch = s[j]

                freq[ch] = freq.get(ch, 0) + 1

                max_freq = max(freq.values())
                min_freq = min(freq.values())

                total += (max_freq - min_freq)

        return total