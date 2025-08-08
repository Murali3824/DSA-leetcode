class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(start,total,path):
            if total == target:
                res.append(path)
                return 
            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if total + candidates[i] > target:
                    break
                backtrack(i + 1, total + candidates[i], path + [candidates[i]])

        backtrack(0,0,[])
        return res
