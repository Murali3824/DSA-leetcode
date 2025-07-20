class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = {}
        n = len(s)

        # Step 1: Build frequency dictionary
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        # Step 2: Find character with max frequency
        max_char = ''
        max_freq = 0
        for ch in freq:
            if freq[ch] > max_freq:
                max_freq = freq[ch]
                max_char = ch

        # Step 3: Check if rearrangement is possible
        if max_freq > (n + 1) // 2:
            return ""

        # Step 4: Create result list
        res = [''] * n
        idx = 0

        # Step 5: Place max_char at even indices
        while freq[max_char] > 0:
            res[idx] = max_char
            idx += 2
            freq[max_char] -= 1

        # Step 6: Place remaining characters
        for ch in freq:
            while freq[ch] > 0:
                if idx >= n:
                    idx = 1  # move to odd indices
                res[idx] = ch
                idx += 2
                freq[ch] -= 1

        return ''.join(res)
        