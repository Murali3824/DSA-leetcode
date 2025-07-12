class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def days_needed(cap):
            day = 1
            load = 0
            for wt in weights:
                if load + wt > cap:
                    day += 1
                    load = wt
                else:
                    load += wt

            return day

        low, high = max(weights), sum(weights)

        while low < high:
            mid = (low + high) // 2
            if days_needed(mid) <= days:
                high = mid
            else:
                low = mid + 1

        return low
        
        