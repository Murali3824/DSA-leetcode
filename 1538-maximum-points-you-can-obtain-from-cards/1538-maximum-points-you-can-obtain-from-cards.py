class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        #sum_left, sum_right = sum(cardPoints[:k]), 0
        #res = sum_left
        #for i in range(k):
        #    sum_left -= cardPoints[k-1-i]
        #    sum_right += cardPoints[len(cardPoints) - 1 - i]
        #    res = max(res, sum_left + sum_right)
        #return res

        n = len(cardPoints)
        total = sum(cardPoints)
        if k == n:
            return total
        
        window_size = n - k
        current_sum = sum(cardPoints[:window_size])
        min_subarray_sum = current_sum
        
        for i in range(window_size, n):
            current_sum += cardPoints[i] - cardPoints[i - window_size]
            min_subarray_sum = min(min_subarray_sum, current_sum)
        
        return total - min_subarray_sum