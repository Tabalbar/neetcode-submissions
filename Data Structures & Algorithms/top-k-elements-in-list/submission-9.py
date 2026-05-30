class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        frequencies = {i:[] for i in range(1, len(nums)+1)}
        top_k = []

        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        for num, freq in counts.items():
            frequencies[freq].append(num)

        for i in range(len(nums), 0, -1):
            for j in range(len(frequencies[i])):
                top_k.append(frequencies[i][j])
                if len(top_k) == k:
                    return top_k
        