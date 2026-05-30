class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}
        frequency_buckets = defaultdict(list)
        top_k = []
        exit_loop = False

        for num in nums:
            if num in num_dict:
                num_dict[num]+=1
            else:
                num_dict[num] = 0
        # Initialize frequency buckets
        for i in range(len(nums)):
            frequency_buckets[i]: []

        for num in num_dict:
            frequency_buckets[num_dict[num]].append(num)

        for i in range(len(nums)-1, -1, -1):
            if (len(frequency_buckets[i])):
                for j in range(len(frequency_buckets[i])):
                    top_k.append(frequency_buckets[i][j])
                    if len(top_k) == k:
                        exit_loop = True
                        break
            if exit_loop:
                break
        return top_k
        

        