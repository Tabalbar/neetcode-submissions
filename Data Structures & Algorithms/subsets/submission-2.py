class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(starting_index, subset):
            for i in range(starting_index, len(nums)):
                subset.append(nums[i])
                dfs(i + 1, subset)
                subset.pop()
            result.append(subset.copy())
        dfs(0, [])
        return result