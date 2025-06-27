class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join(ch * freq for ch, freq in Counter(s).most_common())
        