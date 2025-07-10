class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        if m * k > len(bloomDay):
            return -1

        def possible(day):
            count = 0
            bouq = 0
            for i in bloomDay:
                if i <= day:
                    count += 1
                else:
                    bouq = bouq + (count // k)
                    count = 0
            bouq += (count // k) 
            if bouq >= m:
                return True

        #for i in range(min(bloomDay),max(bloomDay)+1):
        #    if (possible(bloomDay,i,m,k) == True):
        #       return i
        low, high = min(bloomDay), max(bloomDay)

        while low <= high:
            mid = (low + high) // 2
            if possible(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low if low <= max(bloomDay) else -1

        #return -1