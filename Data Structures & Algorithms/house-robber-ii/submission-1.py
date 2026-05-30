class Solution:
    def rob(self, nums: List[int]) -> int:
        def house_robber(sublist):
            rob1, rob2 = 0,0
            for n in sublist:
                tmp = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = tmp
            return rob2
        
        return max(nums[0], house_robber(nums[:-1]), house_robber(nums[1:]))