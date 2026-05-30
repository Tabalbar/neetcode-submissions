class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_bucket = [[] for i in range(1, len(nums) + 1)]
        frequency_dict = {}
        result = []
        for num in nums:
            frequency_dict[num] = 1 + frequency_dict.get(num, 0)

        for num in frequency_dict:
            frequency_bucket[frequency_dict[num]-1].append(num)

        for i in range(len(frequency_bucket)-1, -1, -1):
            if frequency_bucket[i]:
                for j in range(len(frequency_bucket[i])):
                    result.append(frequency_bucket[i][j])
                    if len(result) == k:
                        return result

        return False
        
        