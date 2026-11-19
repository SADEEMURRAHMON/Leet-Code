class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []

        def solve(i, current, total):

            if total == target:
                ans.append(current.copy())
                return

            if total > target or i == len(candidates):
                return

            current.append(candidates[i])
            solve(i, current, total + candidates[i])

            current.pop()
            solve(i + 1, current, total)

        solve(0, [], 0)

        return ans