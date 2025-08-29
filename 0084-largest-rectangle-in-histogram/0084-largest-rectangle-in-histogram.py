class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        def findnse(heights):
            n = len(heights)
            nse = [n]*n
            stack = []
            for i in range(n-1,-1,-1):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                if stack:
                    nse[i] = stack[-1]
                stack.append(i)
            return nse

        def findpse(heights):
            n = len(heights)
            pse = [-1]*n
            stack = []
            for i in range(n):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                if stack:
                    pse[i] = stack[-1]
                stack.append(i)
            return pse
        
        nse = findnse(heights) # [1, 6, 4, 4, 6, 6]
        pse = findpse(heights) # [-1, -1, 1, 2, 1, 4]
        maxi = 0
        for i in range(n):
            maxi = max(maxi,heights[i]*(nse[i]-pse[i]-1))

        return maxi

        
        