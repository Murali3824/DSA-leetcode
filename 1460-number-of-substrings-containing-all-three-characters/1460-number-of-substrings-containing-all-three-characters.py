class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        left = 0
        freq = {}

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1

            while freq.get('a', 0) > 0 and freq.get('b', 0) > 0 and freq.get('c', 0) > 0:
                count += len(s) - right
                freq[s[left]] -= 1
                left += 1

        return count
