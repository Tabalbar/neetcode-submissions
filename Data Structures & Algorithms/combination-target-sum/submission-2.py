class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(total, subset, starting_index):
            if total > target:
                return False
            if total == target:
                result.append(subset.copy())
                return

            for i in range(starting_index, len(nums)):
                subset.append(nums[i])
                dfs(nums[i] + total, subset, i)
                subset.pop()

        dfs(0, [], 0)
        return result