class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}
        for num in nums:
            if num in num_dict:
                num_dict[num]+=1
            else:
                num_dict[num] = 0

        sorted_num_dict = sorted(num_dict.items(), key=lambda x: x[1])
        num_seen = None
        top_k = []
        for i in range(len(sorted_num_dict)-1, -1, -1):
            top_k.append(sorted_num_dict[i][0])
            if len(top_k) == k:
                break
        return top_k