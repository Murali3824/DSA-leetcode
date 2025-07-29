class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""

        t_freq = {}
        for char in t:
            t_freq[char] = t_freq.get(char, 0) + 1

        s_freq = {}
        have, need = 0, len(t_freq)
        left = 0
        min_len = float('inf')
        res = ""

        for right in range(len(s)):
            char = s[right]
            s_freq[char] = s_freq.get(char, 0) + 1

            if char in t_freq and s_freq[char] == t_freq[char]:
                have += 1

            while have == need:
                window_size = right - left + 1
                if window_size < min_len:
                    min_len = window_size
                    res = s[left:right + 1]

                s_freq[s[left]] -= 1
                if s[left] in t_freq and s_freq[s[left]] < t_freq[s[left]]:
                    have -= 1
                left += 1

        return res
