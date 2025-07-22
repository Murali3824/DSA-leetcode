class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        
        maxcount = 0
        for digit in freq:
            if digit-1 not in freq:
                count = 1
                curr_num = digit
                while curr_num+1 in freq:
                    count+=1
                    curr_num += 1
                maxcount = max(maxcount,count)
        return maxcount
             

            
        