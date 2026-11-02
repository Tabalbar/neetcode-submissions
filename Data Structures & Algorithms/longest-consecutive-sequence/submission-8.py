class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0


        lcs = 0
        numSet = set(nums)

        # [2,3,4,5,20]
        # print(buckets)
        for idx,num in enumerate(numSet):
            if num - 1 not in numSet:
                tmpLongest = 1
                lcs = max(lcs, tmpLongest)
                while num + tmpLongest in numSet:
                    tmpLongest += 1
                    lcs = max(lcs, tmpLongest)
                    
                    
        
        return lcs