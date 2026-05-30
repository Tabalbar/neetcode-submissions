class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        prev = -1

        def increment(curr, prev, right):
            while nums[prev] == nums[curr]:
                curr += 1
                if curr >= right:
                    return False
            return curr

        def decrement(curr, prev, left):
            while nums[prev] == nums[curr]:
                curr -= 1
                if curr <= left:
                    return False
            return curr


            

        for i in range(0, len(nums)-2, 1):
            l = i + 1
            r = len(nums)-1
            if prev >= 0:
                while nums[prev] == nums[i]:
                    i += 1
                    if i >= len(nums):
                        break
                    if i >= l:
                        continue
            if i >= l:
                continue
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    l = increment(l, l, r)
                elif total > 0:
                    r = decrement(r, r, l)
                else:
                    l = increment(l, l, r)

                if not l or not r:
                    break
            prev = i

        return result