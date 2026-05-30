from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = defaultdict(int)
        for num in nums:
            nums_dict[num] += 1

        arr = []
        for num, cnt in nums_dict.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        for i in arr[::-1]:
            res.append(i[1])
            if len(res) >= k:
                break
        return res