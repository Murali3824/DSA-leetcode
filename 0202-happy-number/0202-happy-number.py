class Solution:
    def isHappy(self, n: int) -> bool:
        def getNext(n):
            add = 0
            while n > 0:
                d = n % 10
                add += d*d 
                n = n // 10
            return add
    
        while n!=1 and n!=4:
            n = getNext(n)
        return n == 1