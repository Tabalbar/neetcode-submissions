class Solution:
    def search(self, nums: List[int], target: int) -> int:


        l = 0
        r = len(nums) -1

        while(l <= r):
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
        return -1
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         l = 0
#         r = len(nums) - 1  # Right boundary is the last index
        
#         while l <= r:
#             m = l + (r - l) // 2  # Calculate middle index
            
#             if nums[m] == target:  # Found the target
#                 return m
#             elif nums[m] < target:  # Search in the right half
#                 l = m + 1
#             else:  # Search in the left half
#                 r = m - 1
        
#         return -1  # Target not found