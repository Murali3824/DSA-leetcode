class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for digit in nums:
            freq[digit] = freq.get(digit,0) + 1
        
        lists = []
        for key,values in freq.items():
            heapq.heappush(lists,[values,key])
            if len(lists) > k:
                heapq.heappop(lists)
        
        return [values for key,values in lists ]