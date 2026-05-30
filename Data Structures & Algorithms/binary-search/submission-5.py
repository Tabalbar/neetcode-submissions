class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = l + ((r - l)//2)
            value = nums[mid]

            if value == target:
                return mid
            elif value < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1