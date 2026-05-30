class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        counts_as_list = [[] for i in range(len(nums)+1)]
        result = []

        for num in nums:
            count[num] += 1
        
        for num, count in count.items():
            counts_as_list[count].append(num)

        for i in range(len(counts_as_list)-1, 0, -1):
            if len(counts_as_list[i]) > 0:
                for num in counts_as_list[i]:
                    result.append(num)
                    if len(result) == k:
                        return result