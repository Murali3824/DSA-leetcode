class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(start,total,path):
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return
            for i in range(start,len(candidates)):
                path.append(candidates[i])
                backtrack(i,total+candidates[i],path)
                path.pop()
        backtrack(0,0,[])
        return res