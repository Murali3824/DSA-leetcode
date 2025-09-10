class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m_freq = {}
        for char in magazine:
            if char in m_freq:
                m_freq[char] += 1
            else:
                m_freq[char] = 1

        
        for char in ransomNote:
            if char in m_freq and m_freq[char] > 0:
                m_freq[char] -= 1
            else:
                return False
        return True
