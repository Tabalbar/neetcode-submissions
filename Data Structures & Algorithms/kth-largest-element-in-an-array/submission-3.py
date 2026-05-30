class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l, r = 0, len(nums)-1
        kth_largest_element = -1
        index_to_find = len(nums) - k

        def find_kth_largest_element(l, pivot):
            for i in range(l, pivot):
                if nums[i] <= nums[pivot]:
                    tmp = nums[l]
                    nums[l] = nums[i]
                    nums[i] = tmp
                    l += 1
            tmp = nums[pivot]
            nums[pivot] = nums[l]
            nums[l] = tmp
            print(nums, l, k, nums[l])
            if l > index_to_find:
                return find_kth_largest_element(0, l-1) 
            elif l < index_to_find:
                return find_kth_largest_element(l + 1, pivot) 
            else:
                return nums[l]

        return find_kth_largest_element(l, r)
