class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        
        def dfs(i):
            total = sum(subset)
            if total == target:
                res.append(subset.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            subset.append(nums[i])
            dfs(i)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res