class Solution:
    def frequencySort(self, s: str) -> str:
        #return ''.join(ch * freq for ch, freq in Counter(s).most_common())

        freq = {}
        for char in s:
            freq[char] = freq.get(char,0) + 1
        
        freq_list = []
        for char in freq:
            freq_list.append((char,freq[char])) 
        
        for i in range(len(freq_list)):
            for j in range(i+1,len(freq_list)):
                if freq_list[j][1] > freq_list[i][1]:
                    freq_list[j],freq_list[i] = freq_list[i],freq_list[j]
        
        result = ''
        for char,count in freq_list:
            result += char*count
        return result

        