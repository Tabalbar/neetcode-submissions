class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-1,0,1,2,-1,-4]
        # i = -1, j = 1, k = -4
        # missing_complement = -1
        # complement = 1
        # 
        complement_dict = {}
        res = set()
        nums.sort()
        sum_array = []
        j,k = 1,len(nums)-1
        target = 0
        print(nums)
        for i in range(0, len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum_of_integers = nums[j] + nums[k] + nums[i]
                if sum_of_integers == 0:
                    row = [nums[i], nums[j], nums[k]]
                    res.add(tuple(row))
                    k-=1
                    j+=1
                    # if row not in sum_array:
                    #     sum_array.append(row)
                elif sum_of_integers > 0:
                    k-=1
                elif sum_of_integers < 0:
                    j+=1
        return [list(i) for i in res]