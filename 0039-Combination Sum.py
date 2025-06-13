class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def combinations(idx, comb, total):
            if total == target:
                answer.append(comb[:])
                return
            
            if total > target or idx >= len(candidates):
                return
            
            comb.append(candidates[idx])
            combinations(idx, comb, total+candidates[idx])
            comb.pop()
            combinations(idx+1, comb, total)

            return answer

        return combinations(0, [], 0)