class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = {}
        n = len(s)

        for char in s:
            freq[char] = freq.get(char,0) + 1

        max_char = ''
        max_freq = 0
        for char in freq:
            if freq[char] > max_freq:
                max_freq = freq[char]
                max_char = char
        if max_freq > (n+1) // 2:
            return ""

        result = ['']*n
        idx = 0
        while freq[max_char] > 0:
            result[idx] = max_char
            idx += 2
            freq[max_char] -= 1
        
        for char in freq:
            while freq[char] > 0:
                if idx >= n:
                    idx = 1
                result[idx] = char
                idx += 2
                freq[char] -= 1
        return ''.join(result)    

            
                  